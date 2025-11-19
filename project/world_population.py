# World Population Dashboard (Streamlit)
# Save this file as `world_population_dashboard.py` and run with:
#    pip install streamlit pandas plotly
#    streamlit run world_population_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

st.set_page_config(layout="wide", page_title="World Population Dashboard")

@st.cache_data
def load_population_data():
    # Primary source: Our World in Data (kept on GitHub)
    url = (
        "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Population%20(OWID)/Population%20(OWID).csv"
    )
    try:
        df = pd.read_csv(url)
    except Exception:
        # Fallback generic population dataset
        url2 = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
        df = pd.read_csv(url2)
        # normalize column names if using fallback
        df = df.rename(columns={"Country Name": "entity", "Year": "year", "Value": "population"})
        # try to add iso_code column (may be missing)
        df["iso_code"] = None

    # Standardize column names for OWID format
    df.columns = [c.strip() for c in df.columns]
    # OWID columns include: entity, code (iso_code), year, population
    if "code" in df.columns and "population" in df.columns:
        df = df.rename(columns={"code": "iso_code"})
    # Ensure lower/consistent types
    if "year" in df.columns:
        df["year"] = df["year"].astype(int)
    if "population" in df.columns:
        df["population"] = pd.to_numeric(df["population"], errors="coerce")

    return df

# Load data
with st.spinner("Loading population data..."):
    pop = load_population_data()

# Basic checks
if "entity" not in pop.columns:
    st.error("Loaded dataset doesn't have the expected columns. Inspect the CSV URL or provide a CSV with columns: entity, iso_code (or code), year, population.")
    st.stop()

# Sidebar: Filters
st.sidebar.header("Filters")
min_year = int(pop["year"].min())
max_year = int(pop["year"].max())
selected_year = st.sidebar.slider("Select year", min_year, max_year, max_year)

all_regions = None
if "region" in pop.columns:
    all_regions = pop["region"].dropna().unique().tolist()

# Country multiselect
countries = sorted(pop["entity"].unique().tolist())
selected_countries = st.sidebar.multiselect("Select countries (for trend & top lists)", countries, ["India", "United States"] if "India" in countries else countries[:2])

# Top N selector
top_n = st.sidebar.number_input("Top N countries by population (bar chart)", min_value=5, max_value=50, value=10)

# Population range filter
min_pop = float(pop.loc[pop["year"] == selected_year, "population"].min())
max_pop = float(pop.loc[pop["year"] == selected_year, "population"].max())
pop_range = st.sidebar.slider("Population range (selected year)", min_value=0.0, max_value=max_pop, value=(min_pop, max_pop))

st.title("🌍 World Population Dashboard")
st.markdown(
    "Interactive dashboard showing global population trends. Use the sidebar to filter year, countries and population ranges. Data source: Our World in Data / public CSVs."
)

# Key metrics for the selected year
year_df = pop[pop["year"] == selected_year].copy()
# apply pop range filter
year_df = year_df[(year_df["population"] >= pop_range[0]) & (year_df["population"] <= pop_range[1])]

world_pop = year_df["population"].sum()
largest = year_df.sort_values("population", ascending=False).head(1)
largest_name = largest.iloc[0]["entity"] if not largest.empty else "N/A"
largest_pop = int(largest.iloc[0]["population"]) if not largest.empty else 0

col1, col2, col3 = st.columns(3)
col1.metric("Year", selected_year)
col2.metric("World population (selected year)", f"{int(world_pop):,}")
col3.metric("Largest country (selected year)", f"{largest_name} — {largest_pop:,}")

# Choropleth map
st.subheader("World choropleth — population by country")
map_df = year_df.dropna(subset=["population"]).copy()
# Some datasets use iso_code or code; Plotly expects ISO Alpha-3
iso_col = "iso_code" if "iso_code" in map_df.columns else None

if iso_col is None or map_df[iso_col].isnull().all():
    st.warning("No ISO codes available in dataset — the choropleth may not render correctly. Consider providing a dataset with ISO Alpha-3 codes.")
    # try to skip map
else:
    fig_map = px.choropleth(
        map_df,
        locations=iso_col,
        color="population",
        hover_name="entity",
        projection="natural earth",
        title=f"Population in {selected_year}",
        labels={"population": "Population"},
    )
    fig_map.update_layout(height=500, margin=dict(l=10, r=10, t=60, b=10))
    st.plotly_chart(fig_map, use_container_width=True)

# Top N bar chart
st.subheader(f"Top {top_n} countries by population — {selected_year}")
top_df = year_df.sort_values("population", ascending=False).head(top_n).copy()
fig_bar = px.bar(top_df, x="population", y="entity", orientation="h", title=f"Top {top_n} by population ({selected_year})")
fig_bar.update_layout(yaxis=dict(autorange="reversed"), height=450)
st.plotly_chart(fig_bar, use_container_width=True)

# Trend lines for selected countries
st.subheader("Population trends over time")
if len(selected_countries) == 0:
    st.info("Select one or more countries in the sidebar to see trend lines.")
else:
    trend_df = pop[pop["entity"].isin(selected_countries)].dropna(subset=["population"]) 
    fig_line = px.line(trend_df, x="year", y="population", color="entity", markers=True, title="Population over time")
    fig_line.update_layout(height=450)
    st.plotly_chart(fig_line, use_container_width=True)

# Optional: region breakdown if region column present
if all_regions:
    st.subheader("Population by region (selected year)")
    reg_df = year_df.groupby("region")["population"].sum().reset_index().sort_values("population", ascending=False)
    fig_pie = px.pie(reg_df, names="region", values="population", title=f"Population by region — {selected_year}")
    st.plotly_chart(fig_pie, use_container_width=True)

# Data explorer / download
st.subheader("Data explorer")
with st.expander("View & download filtered data"):
    st.write("Data filtered by your sidebar selections:")
    display_df = pop.copy()
    # apply filters
    display_df = display_df[display_df["year"] == selected_year]
    display_df = display_df[(display_df["population"] >= pop_range[0]) & (display_df["population"] <= pop_range[1])]
    if len(selected_countries) > 0:
        display_df = display_df[display_df["entity"].isin(selected_countries)]
    st.dataframe(display_df.reset_index(drop=True))
    csv = display_df.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name=f"population_{selected_year}.csv", mime="text/csv")

# Footer / tips
st.markdown("---")
st.markdown(
    "**Tips:** Use the year slider to inspect historical snapshots, pick countries to compare growth, and change Top N to focus the bar chart. If the choropleth doesn't render, provide data with ISO Alpha-3 country codes (e.g., USA, IND, CHN)."
)

# End of app
