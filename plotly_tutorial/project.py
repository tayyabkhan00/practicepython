from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

x = np.arange(1, 51)
y = np.random.randint(10, 100, 50)

fig = make_subplots(
    rows=5, cols=2,
    specs=[
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "xy"}, {"type": "domain"}],  # pie chart cell
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "xy"}, {"type": "xy"}],
    ]
)

fig.add_trace(go.Scatter(x=x, y=y), 1,1)
fig.add_trace(go.Bar(x=x, y=y), 1,2)
fig.add_trace(go.Scatter(x=x, y=y, mode='markers'), 2,1)
fig.add_trace(go.Histogram(x=y), 2,2)
fig.add_trace(go.Box(y=y), 3,1)
fig.add_trace(go.Pie(labels=["A","B","C"], values=[30,40,30]), 3,2)
fig.add_trace(go.Scatter(x=x[:20], y=y[:20]), 4,1)
fig.add_trace(go.Scatter(x=x, y=np.cumsum(np.random.randn(50))), 4,2)
fig.add_trace(go.Violin(y=y), 5,1)
fig.add_trace(go.Scatter(x=sorted(y), y=np.linspace(0,1,50)), 5,2)

fig.update_layout(height=1500, width=900, title="10-Plot Dashboard")
fig.show()

