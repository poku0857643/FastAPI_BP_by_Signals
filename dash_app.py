# dependencies for visualizer
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import httpx
import asyncio
from fastapi.responses import JSONResponse

sbp_prediction_list = [120.0, 121.5, 135.0, 140.2]
dbp_prediction_list = [80.0, 81.0, 85.0, 88.0]


# prediction visualizer
dash_app = dash.Dash(__name__)
dash_app.title = "Blood Pressure Prediction Visualizer"



# html layout of visualizer
dash_app.layout =html.Div([
    html.H1("Blood Pressure Prediction Visualizer", style = {'textAlign': 'center'}),
    dcc.Graph(id='bp-visualization'),
    html.Button('Update Data', id='update-btn', n_clicks=0, style={'margin': '20px'})
])

# predict_bp_endpoint = app.server.endpoint(predict_bp_endpoint)

async def fetch_predictions():
    async with httpx.AsyncClient() as client:
        response = await client.get(dash_app.server.url_for("predict_bp_endpoint"))
        response.raise_for_status()
        data = response.json()
        return data.get("sbp", []), data.get("dbp", [])


@dash_app.callback(
    Output('bp-visualization', 'figure'),
    Input('update-btn', 'n_clicks')
)

def update_graph(n_clicks, sbp_test_list = sbp_prediction_list, dbp_test_list = dbp_prediction_list):
    if n_clicks == 0:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[0], y=sbp_test_list, mode="lines+markers", name="SBP"))
        fig.add_trace(go.Scatter(x=[0], y=dbp_test_list, mode="lines+markers", name="DBP"))
        fig.update_layout(title="Blood Pressure Prediction", xaxis_title="Data Points", yaxis_title="BP Values [mmHg]",
                          template="plotly_white")
        return fig

    try:
        sbp_prediction_list, dbp_prediction_list = asyncio.run(fetch_predictions())
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(range(len(sbp_prediction_list))), y=sbp_prediction_list, mode="lines+markers", name="SBP"))
        fig.add_trace(go.Scatter(x=list(range(len(dbp_prediction_list))), y=dbp_prediction_list, mode="lines+markers", name="DBP"))
        fig.update_layout(title="Blood Pressure Prediction", xaxis_title="Data Points", yaxis_title="BP Values [mmHg]", template="plotly_white")
        return fig

    except Exception as e:
        return go.Figure()

if __name__ == "__main__":
    dash_app.run_server(debug=True, port=8050)


