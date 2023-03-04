import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime, time, timedelta

# Importer les données depuis le fichier csv
df = pd.read_csv('/home/ec2-user/Projet_Linux_Python/Prix.csv', names = ['date', 'prix'])
df['date'] = pd.to_datetime(df['date'])
min_price = min(df['prix'])
max_price = max(df['prix'])

# print(datetime.now())

# Créer le graphique initial
graphique = go.Scatter(x=df['date'], y=df['prix'], mode='lines', line=dict(color='#34A853'), fill='tonexty', fillcolor='rgba(52,168,83,0.3)')

def generate_table():
    # Get the data for the current day
    today = datetime.now().date()
    today_start = datetime.combine(today, time.min)
    today_end = datetime.combine(today, time.max)
    df_today = df.loc[(df['date'] >= today_start) & (df['date'] <= today_end)]

    # Calculate the required metrics
    variation = round((df_today['prix'].iloc[-1] - df_today['prix'].iloc[0]) / df_today['prix'].iloc[0] * 100, 2)
    min_price = round(df_today['prix'].min(), 2)
    max_price = round(df_today['prix'].max(), 2)
    daily_volatility = round(df_today['prix'].std(), 2)
    price_return = round((df_today['prix'].iloc[-1] - df_today['prix'].iloc[0]) / df_today['prix'].iloc[0] * 100, 2)

    # Create the table
    table = html.Div([
        html.H3("Tableau de Synthèse {}".format(today.strftime('%d-%m-%Y')), style={'text-align': 'center'}),
        html.Table([
            html.Thead(html.Tr([html.Th('Metric'), html.Th('Value')])),
            html.Tbody([
                html.Tr([html.Td('Variation'), html.Td('{}%'.format(variation))]),
                html.Tr([html.Td('Min price'), html.Td(min_price)]),
                html.Tr([html.Td('Max price'), html.Td(max_price)]),
                html.Tr([html.Td('Daily volatility'), html.Td(daily_volatility)]),
                html.Tr([html.Td('Price return'), html.Td('{}%'.format(price_return))]),
                html.Tr([html.Td('First price'), html.Td(df_today['prix'].iloc[0])]),
                html.Tr([html.Td('Last price'), html.Td(df_today['prix'].iloc[-1])])
        ])
    ], className='table', style={'margin': 'auto'})
    ])

    return table




def generate_table_yesterday():
    # Get the data for yesterday
    yesterday = datetime.now().date() - timedelta(days=1)
    yesterday_start = datetime.combine(yesterday, time.min)
    yesterday_end = datetime.combine(yesterday, time.max)
    df_yesterday = df.loc[(df['date'] >= yesterday_start) & (df['date'] <= yesterday_end)]

    # Calculate the required metrics for yesterday
    variation = round((df_yesterday['prix'].iloc[-1] - df_yesterday['prix'].iloc[0]) / df_yesterday['prix'].iloc[0] * 100, 2)
    min_price = round(df_yesterday['prix'].min(), 2)
    max_price = round(df_yesterday['prix'].max(), 2)
    daily_volatility = round(df_yesterday['prix'].std(), 2)
    price_return = round((df_yesterday['prix'].iloc[-1] - df_yesterday['prix'].iloc[0]) / df_yesterday['prix'].iloc[0] * 100, 2)

    # Create the table for yesterday
    table = html.Div([
        html.H3("Tableau de Synthèse {}".format(yesterday.strftime('%d-%m-%Y')), style={'text-align': 'center'}),
        html.Table([    
            html.Thead(html.Tr([html.Th('Metric'), html.Th('Value')])),
            html.Tbody([        
                html.Tr([html.Td('Variation'), html.Td('{}%'.format(variation))]),
                html.Tr([html.Td('Min price'), html.Td(min_price)]),
                html.Tr([html.Td('Max price'), html.Td(max_price)]),
                html.Tr([html.Td('Daily volatility'), html.Td(daily_volatility)]),
                html.Tr([html.Td('Price return'), html.Td('{}%'.format(price_return))]),
                html.Tr([html.Td('First price'), html.Td(df_yesterday['prix'].iloc[0])]),
                html.Tr([html.Td('Last price'), html.Td(df_yesterday['prix'].iloc[-1])])
        ])
    ], className='table', style={'margin': 'auto'})
    ])

    return table



def get_table():
    now = datetime.now()
    today_at_8pm = datetime.combine(now.date(), time(hour=20))
    if now.hour >= today_at_8pm.hour:
        return generate_table()
    else:
        return generate_table() #_yesterday()


# Créer le tableau de bord
app = dash.Dash(__name__)
app.layout = html.Div(className='container', children=[
        html.Div(className='header', children=[
            html.Div(className='title', children=[
                html.H1(children='Tableau de bord financier : Cardano ADA/EUR', style={'text-align': 'center', 'border': '1px solid #ddd', 'border-radius': '10px'})
        ]),
        html.Div(className='subtitle', children=[
            html.H2(id='last-price', children='Dernier prix : {}'.format(df['prix'].iloc[-1]), style={'text-align': 'center'}),
            html.H2(id='last-date', children='Dernière Date : {}'.format(df['date'].iloc[-1]), style={'text-align': 'center'})
        ])
    ]),
    html.Div(className='content', children=[
        html.Div(className='options', children=[
            html.H3(children='Durée :'),
            dcc.RadioItems(
              id='duree',
              options=[
                {'label': '1h', 'value': '1h'},
                {'label': '5h', 'value': '5h'},
                {'label': '1j', 'value': '1j'},
                {'label': '1 semaine', 'value': '1s'},
                {'label': '1 mois', 'value': '1m'},
                {'label': 'Max', 'value': 'max'}
            ],
            value='1j'
            )
        ]),
        html.Div(className='graph-container', children=[
            dcc.Graph(id='graphique', figure={'data': [graphique], 'layout': {'yaxis': {'range': [min_price, max_price]}}})
        ]),
    ], style={'border': '1px solid #ddd', 'border-radius': '5px'}),
    html.Div(className='table-container', children=get_table(), style={'border': '1px solid #ddd', 'border-radius': '10px', 'margin-top': '20px'})
], style={
    'margin': '0 auto',
    'max-width': '800px',
    'font-family': 'Arial, sans-serif'
})

# Callback pour mettre à jour le graphique en fonction de la durée sélectionnée
@app.callback(Output('graphique', 'figure'), [Input('duree', 'value')])
def update_figure(duree):
    if duree == '1h':
        df_filtre = df.tail(12)
    elif duree == '5h':
        df_filtre = df.tail(60)
    elif duree == '1j':
        df_filtre = df.tail(288)
    elif duree == '1s':
        df_filtre = df.tail(2016)
    elif duree == '1m':
        df_filtre = df.tail(8064)
    elif duree == 'max':
        df_filtre = df.tail(len(df))
    else:
        df_filtre = df
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_filtre['date'], y=df_filtre['prix'], mode='lines', line=dict(color='#34A853'), fill='tonexty', fillcolor='rgba(52,168,83,0.3)'))
    fig.update_layout(transition_duration=500, yaxis={'range': [min_price, max_price]})
    return fig

# Lancer l'application
if __name__ == '__main__':
    app.run_server(host = "0.0.0.0", port = 8050, debug=True)
