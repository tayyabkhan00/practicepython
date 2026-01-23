import streamlit as st
import pickle
import json
import numpy as np
import os

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Bengaluru House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# -------------------------------
# Background + Styling
# -------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(
            rgba(0,0,0,0.55),
            rgba(0,0,0,0.55)
        ),
        url("https://images.pexels.com/photos/4119830/pexels-photo-4119830.jpeg?_gl=1*fc89kq*_ga*MTU5Mjk0MjQwLjE3NjkwOTA1NTE.*_ga_8JE65Q40S6*czE3NjkxMDM0ODEkbzQkZzEkdDE3NjkxMDM0OTYkajQ1JGwwJGgw");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    h1, h2, h3, label {
        color: white !important;
    }

    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 0.5em 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Load model safely (Cloud-safe)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model", "house_price_model.pkl")
columns_path = os.path.join(BASE_DIR, "model", "columns.json")

model = pickle.load(open(model_path, "rb"))
columns = json.load(open(columns_path, "r"))

# -------------------------------
# App UI
# -------------------------------
st.title("🏠 Bengaluru House Price Predictor")

st.markdown("### Enter House Details")

# Input fields
exclude_cols = ['total_sqft', 'bath', 'bhk']
locations = sorted([c for c in columns if c not in exclude_cols])

location = st.selectbox("📍 Location", locations)
sqft = st.number_input("📐 Total Square Feet", min_value=300.0, step=50.0)
bath = st.number_input("🛁 Bathrooms", min_value=1, step=1)
bhk = st.number_input("🛏️ BHK", min_value=1, step=1)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Price"):
    try:
        x = np.zeros(len(columns))

        x[columns.index('total_sqft')] = sqft
        x[columns.index('bath')] = bath
        x[columns.index('bhk')] = bhk

        if location in columns:
            x[columns.index(location)] = 1

        import pandas as pd
        x_df = pd.DataFrame([x], columns=columns)

        price = model.predict(x_df)[0]

        st.success(f"💰 Estimated Price: ₹ {round(price, 2)} Lakhs")

    except Exception as e:
        st.error("❌ Prediction failed")
        st.code(str(e))


