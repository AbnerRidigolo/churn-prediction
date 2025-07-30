import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Carregar dados
df = pd.read_csv('../data/telco_churn.csv')
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Inicializar app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("📊 Dashboard de Churn - Telco", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='coluna',
        options=[{'label': col, 'value': col} for col in ['Contract', 'PaymentMethod', 'InternetService']],
        value='Contract'
    ),
    dcc.Graph(id='grafico')
])

# Callback
@app.callback(
    dash.dependencies.Output('grafico', 'figure'),
    [dash.dependencies.Input('coluna', 'value')]
)
def update_graph(coluna):
    fig = px.histogram(df, x=coluna, color='Churn', barmode='group',
                       title=f'Distribuição de Churn por {coluna}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
