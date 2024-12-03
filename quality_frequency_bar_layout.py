import pandas as pd
from dash import dcc, html
import plotly.express as px

red_wine = pd.read_csv('winequality-red.csv', sep=';')
white_wine = pd.read_csv('winequality-white.csv', sep=';')

def create_quality_frequency_bar_layout():
    red_quality_counts = red_wine['quality'].value_counts().reset_index()
    white_quality_counts = white_wine['quality'].value_counts().reset_index()

    red_quality_counts.columns = ['quality', 'count']
    white_quality_counts.columns = ['quality', 'count']

    red_quality_counts['type'] = 'Vinho Tinto'
    white_quality_counts['type'] = 'Vinho Branco'

    combined = pd.concat([red_quality_counts, white_quality_counts])

    fig = px.bar(
        combined,
        x='quality',
        y='count',
        color='type',
        barmode='group',
        title='Frequência de Notas de Qualidade por Tipo de Vinho',
        labels={'quality': 'Qualidade', 'count': 'Frequência'},
        color_discrete_map={'Vinho Tinto': '#5D1C34', 'Vinho Branco': '#3C5759'}
    )

    return html.Div([
        html.H2("Frequência de Notas de Qualidade"),
        dcc.Graph(figure=fig)
    ], style={'width': '48%', 'padding': '10px'})
