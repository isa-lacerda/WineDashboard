import pandas as pd
from dash import dcc, html, Input, Output
import plotly.express as px

red_wine = pd.read_csv('winequality-red.csv', sep=';')
white_wine = pd.read_csv('winequality-white.csv', sep=';')

def create_regression_scatter_layout(app):
    layout = html.Div([
        html.H2("Regressão Linear: Teor Alcoólico vs Qualidade"),
        dcc.Dropdown(
            id="regression-wine-type-selector",  
            options=[
                {"label": "Vinho Tinto", "value": "red"},
                {"label": "Vinho Branco", "value": "white"}
            ],
            value="red",
            placeholder="Selecione o tipo de vinho",
            style={"width": "50%", "margin-bottom": "20px"}
        ),
        dcc.Graph(id="regression-scatter"),
    ], style={'width': '100%', 'padding': '10px'})

    
    @app.callback(
        Output("regression-scatter", "figure"),
        Input("regression-wine-type-selector", "value")  
    )
    def update_regression_scatter(wine_type):
        if wine_type == "red":
            data = red_wine
            title = "Regressão Linear: Teor Alcoólico vs Qualidade (Vinho Tinto)"
            color = "darkred"
        else:
            data = white_wine
            title = "Regressão Linear: Teor Alcoólico vs Qualidade (Vinho Branco)"
            color = "darkblue"

        fig = px.scatter(
            data, x='alcohol', y='quality', trendline="ols",
            title=title,
            labels={'alcohol': 'Teor Alcoólico (%)', 'quality': 'Qualidade'},
            color_discrete_sequence=[color]
        )

        return fig

    return layout
