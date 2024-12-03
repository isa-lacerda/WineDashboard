from dash import Dash, html
from layouts.correlation_heatmap_layout import create_correlation_heatmap_layout
from layouts.mean_comparison_layout import create_mean_comparison_layout
from layouts.regression_scatter_layout import create_regression_scatter_layout
from layouts.quality_frequency_bar_layout import create_quality_frequency_bar_layout

app = Dash(__name__, external_stylesheets=["/assets/style.css"])

app.layout = html.Div(children=[
    html.Div(className="navbar", children=[
        html.H1("Análise de Vinhos")
    ]),

    html.Div(children=[
        create_correlation_heatmap_layout(app),
        create_mean_comparison_layout(),
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'margin-bottom': '20px'}),

    html.Div(children=[
        create_quality_frequency_bar_layout(),
        create_regression_scatter_layout(app),
    ], style={'display': 'flex', 'justifyContent': 'space-between'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
