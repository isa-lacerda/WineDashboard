import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output

# Carregar os dados
red_wine = pd.read_csv('winequality-red.csv', sep=';')
white_wine = pd.read_csv('winequality-white.csv', sep=';')

# Layout com interação
def create_correlation_heatmap_layout(app):
    variables = red_wine.columns

    layout = html.Div(
        children=[
            html.H2("Mapa de Correlação"),
            dcc.RadioItems(
                id="wine-type-selector",
                options=[
                    {"label": "Vinho Tinto", "value": "red"},
                    {"label": "Vinho Branco", "value": "white"}
                ],
                value="red",
                inline=True
            ),
            dcc.Dropdown(
                id="variable-selector",
                options=[{"label": col, "value": col} for col in variables],
                value=variables[:5],
                multi=True,
                placeholder="Selecione as variáveis para o heatmap"
            ),
            dcc.Graph(
                id="correlation-heatmap",
                style={
                    "width": "90%",
                    "height": "600px",
                    "margin": "auto"
                }
            )
        ],
        style={
            "margin-left": "20px",
            "padding": "10px"
        }
    )

    @app.callback(
        Output("correlation-heatmap", "figure"),
        Input("wine-type-selector", "value"),
        Input("variable-selector", "value")
    )
    def update_heatmap(wine_type, selected_vars):
        if wine_type == "red":
            data = red_wine
        else:
            data = white_wine

        if not selected_vars or len(selected_vars) < 2:
            return px.imshow([], text_auto=True, title="Selecione pelo menos 2 variáveis")

        corr_matrix = data[selected_vars].corr()

        fig = px.imshow(
            corr_matrix,
            text_auto=True,
            color_continuous_scale="Viridis",
            labels={"color": "Correlação"},
            title="Heatmap de Correlação"
        )
        fig.update_layout(
            autosize=False,
            width=800,
            height=600
        )
        return fig

    return layout
