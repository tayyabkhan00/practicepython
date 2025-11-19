import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Load dataset
df = px.data.iris()

# Dark + Light themes
THEMES = {
    "Light": dbc.themes.FLATLY,
    "Dark": dbc.themes.DARKLY
}

app = dash.Dash(__name__, external_stylesheets=[THEMES["Light"]])
app.title = "Advanced Iris Dashboard"

app.layout = dbc.Container([
    
    dbc.Row([
        # Sidebar
        dbc.Col([
            html.H2("🌸 Iris Dashboard", className="text-center mt-4"),
            
            html.Hr(),
            
            # Theme toggle
            html.Label("Theme:", className="fw-bold"),
            dcc.Dropdown(
                id="theme-switch",
                options=[{"label": k, "value": v} for k, v in THEMES.items()],
                value=THEMES["Light"],
                clearable=False,
                className="mb-3"
            ),

            # Page selector
            html.Label("Page:", className="fw-bold"),
            dcc.RadioItems(
                id="page-selector",
                options=[
                    {"label": "Overview", "value": "overview"},
                    {"label": "Visual Analysis", "value": "viz"},
                    {"label": "3D & Advanced", "value": "advanced"},
                    {"label": "Data Table", "value": "table"}
                ],
                value="overview",
                className="mt-2"
            ),
        ], width=2, className="bg-light p-3 border rounded"),

        # Main content
        dbc.Col([
            html.Div(id="main-content", className="p-4")
        ], width=10)
    ])
], fluid=True)


# ----------- CALLBACK FOR MAIN CONTENT + THEME SWITCH -----------

@app.callback(
    dash.dependencies.Output("main-content", "children"),
    [
        dash.dependencies.Input("page-selector", "value"),
        dash.dependencies.Input("theme-switch", "value")
    ]
)
def update_page(page, theme):

    template = "plotly_white" if "FLATLY" in theme else "plotly_dark"

    kpi_row = dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Average Petal Length", className="text-center"),
                html.H2(round(df["petal_length"].mean(), 2), className="text-center text-primary")
            ])
        ], className="shadow-sm")),
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Average Sepal Width", className="text-center"),
                html.H2(round(df["sepal_width"].mean(), 2), className="text-center text-success")
            ])
        ], className="shadow-sm")),
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Total Samples", className="text-center"),
                html.H2(len(df), className="text-center text-danger")
            ])
        ], className="shadow-sm")),
    ], className="mt-4 mb-4")

    if page == "overview":
        return [
            html.H3("📌 Overview", className="mb-4"),
            kpi_row,
            dcc.Graph(figure=px.scatter(
                df, x="sepal_length", y="petal_length",
                color="species", size="sepal_width",
                title="Scatter Plot: Sepal vs Petal",
                template=template
            ))
        ]

    elif page == "viz":
        return [
            html.H3("📊 Visual Analysis", className="mb-4"),

            dcc.Graph(figure=px.histogram(
                df, x="sepal_width", color="species",
                nbins=20, title="Sepal Width Distribution",
                template=template
            )),

            dcc.Graph(figure=px.box(
                df, x="species", y="petal_length",
                title="Petal Length by Species",
                color="species", template=template
            )),

            dcc.Graph(figure=px.violin(
                df, x="species", y="sepal_length", box=True,
                title="Violin Plot of Sepal Length",
                template=template
            ))
        ]

    elif page == "advanced":
        return [
            html.H3("🧪 Advanced Visualizations", className="mb-4"),

            dcc.Graph(figure=px.scatter_3d(
                df, x="sepal_length", y="sepal_width", z="petal_length",
                color="species", title="3D Scatter Plot",
                template=template
            )),

            dcc.Graph(figure=px.scatter_matrix(
                df, dimensions=df.columns[:4], color="species",
                title="Scatter Matrix (Pair Plot)",
                template=template
            ))
        ]

    elif page == "table":
        return [
            html.H3("📄 Data Table", className="mb-4"),
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records"),
                filter_action="native",
                sort_action="native",
                page_size=10,
                style_table={"overflowX": "auto"},
                style_cell={"textAlign": "center"},
                style_header={"backgroundColor": "lightgray", "fontWeight": "bold"}
            )
        ]

    return html.H3("Page Not Found")

# Run App
if __name__ == "__main__":
    app.run(debug=True)
