import pandas as pd
from dash import dcc, html, Input, Output, callback
import plotly.graph_objects as go

red_wine = pd.read_csv('winequality-red.csv', sep=';')
white_wine = pd.read_csv('winequality-white.csv', sep=';')

def create_mean_comparison_layout():
    variables = red_wine.select_dtypes(include='number').columns

    return html.Div([
        html.H2("Comparação de Médias por Variável"),
        dcc.Dropdown(
            id='variable-dropdown',
            options=[{'label': var, 'value': var} for var in variables],
            value='alcohol',  
            placeholder='Selecione uma variável'
        ),
        dcc.Graph(id='mean-comparison-graph')
    ], style={'width': '48%', 'padding': '10px'})

@callback(
    Output('mean-comparison-graph', 'figure'),
    Input('variable-dropdown', 'value')
)
def update_mean_comparison(variable):
    mean_red = red_wine[variable].mean()
    mean_white = white_wine[variable].mean()

    fig = go.Figure(data=[
        go.Bar(name='Vinho Tinto', x=['Vinho Tinto'], y=[mean_red], marker_color='#5D1C34'),
        go.Bar(name='Vinho Branco', x=['Vinho Branco'], y=[mean_white], marker_color='#3C5759'),
    ])
    fig.update_layout(
        title=f"Média de {variable.capitalize()} por Tipo de Vinho",
        xaxis_title="Tipo de Vinho",
        yaxis_title=f"Média de {variable.capitalize()}",
        barmode='group'
    )
    return fig
