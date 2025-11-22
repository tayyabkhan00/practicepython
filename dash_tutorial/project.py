import dash
from dash import dcc, html
import plotly.express as px
import numpy as np
import pandas as pd

# ----------- Generate sample data -----------
np.random.seed(42)
df = pd.DataFrame({
    "x": np.arange(1, 51),
    "y": np.random.randint(10, 100, 50),
    "cat": np.random.choice(["A","B","C"], 50),
    "value": np.random.randn(50).cumsum()
})

# ----------- Create 10 simple charts -----------
fig1 = px.line(df, x="x", y="y")
fig2 = px.bar(df, x="cat", y="y")
fig3 = px.scatter(df, x="x", y="value")
fig4 = px.histogram(df, x="y")
fig5 = px.box(df, y="y")
fig6 = px.area(df, x="x", y="value")
fig7 = px.pie(df, names="cat")
fig8 = px.violin(df, y="y")
fig9 = px.strip(df, x="cat", y="y")
fig10 = px.ecdf(df, x="y")

# ----------- Build Dashboard -----------
app = dash.Dash()

app.layout = html.Div([
    html.H1("10-Plot Dashboard (No Internet Data)", style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        dcc.Graph(figure=fig7),
        dcc.Graph(figure=fig8),
        dcc.Graph(figure=fig9),
        dcc.Graph(figure=fig10),
    ], style={"columnCount": 2})  # 2 columns layout
])

if __name__ == "__main__":
    app.run(debug=True)
