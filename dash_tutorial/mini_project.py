
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Load dataset
df = px.data.iris()

# App with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Layout
app.layout = dbc.Container([

    dbc.Row([
        dbc.Col(html.H1("🌸 Iris Species Dashboard",
                        className="text-center mt-4 mb-4"),
                width=12)
    ]),

    # Filters Section
    dbc.Row([
        dbc.Col([
            html.Label("Select Species:", className="fw-bold"),
            dcc.Dropdown(
                id="species-dropdown",
                options=[{"label": s, "value": s} for s in df["species"].unique()] +
                        [{"label": "All", "value": "All"}],
                value="All",
                clearable=False
            )
        ], width=4)
    ], className="mb-4"),

    # KPIs Section
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Average Petal Length", className="card-title text-center"),
                html.H3(id="avg-petal", className="text-center text-primary")
            ])
        ], color="light"), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Average Sepal Width", className="card-title text-center"),
                html.H3(id="avg-sepal", className="text-center text-success")
            ])
        ], color="light"), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Total Samples", className="card-title text-center"),
                html.H3(id="count", className="text-center text-danger")
            ])
        ], color="light"), width=4),
    ], className="mb-4"),

    # Graphs Section
    dbc.Row([
        dbc.Col(dcc.Graph(id="scatter-plot"), width=6),
        dbc.Col(dcc.Graph(id="hist-plot"), width=6)
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id="box-plot"), width=12)
    ])

], fluid=True)


# Callbacks
@app.callback(
    [
        dash.dependencies.Output("scatter-plot", "figure"),
        dash.dependencies.Output("hist-plot", "figure"),
        dash.dependencies.Output("box-plot", "figure"),
        dash.dependencies.Output("avg-petal", "children"),
        dash.dependencies.Output("avg-sepal", "children"),
        dash.dependencies.Output("count", "children")
    ],
    [dash.dependencies.Input("species-dropdown", "value")]
)
def update_dashboard(selected_species):

    # Filter data
    if selected_species == "All":
        dff = df.copy()
    else:
        dff = df[df["species"] == selected_species]

    # KPIs
    avg_petal = round(dff["petal_length"].mean(), 2)
    avg_sepal = round(dff["sepal_width"].mean(), 2)
    count = len(dff)

    # Scatter Plot
    scatter_fig = px.scatter(
        dff,
        x="sepal_length",
        y="petal_length",
        color="species",
        size="petal_width",
        title="Sepal Length vs Petal Length",
        template="plotly_white"
    )

    # Histogram
    hist_fig = px.histogram(
        dff,
        x="sepal_width",
        nbins=20,
        color="species",
        title="Distribution of Sepal Width",
        template="plotly_white"
    )

    # Box Plot
    box_fig = px.box(
        dff,
        x="species",
        y="petal_length",
        color="species",
        title="Petal Length by Species",
        template="plotly_white"
    )

    return scatter_fig, hist_fig, box_fig, avg_petal, avg_sepal, count


# Run app
if __name__ == "__main__":
    app.run(debug=True)
