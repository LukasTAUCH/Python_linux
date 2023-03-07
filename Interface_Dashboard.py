# Importation des librairies 
# Dash pour la création du serveur 
# Pandas pour la gestion du dataframe qui est notre csv avec notre donnée et date.
# plotly pour la création de gaph.
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime, time, timedelta

# Importer les données depuis le fichier csv de notre donnée récupérée 
df = pd.read_csv('/home/ec2-user/Projet_Linux_Python/Prix.csv', names = ['date', 'prix'])
df['date'] = pd.to_datetime(df['date'])  # la date avec était un string, on le converte en date
min_price = min(df['prix'])
max_price = max(df['prix'])

# Créer le graphique avec pour abscisse les dates
# et pour ordonner les prix 
# je change aussi la couleur en vert et met du vert en dessous de la courbe
graphique = go.Scatter(x=df['date'], y=df['prix'], mode='lines', line=dict(color='#34A853'), fill='tonexty', fillcolor='rgba(52,168,83,0.3)')


# Fonction qui retourne un tableau pour notre analyse de 20h
def generate_table():
    today = datetime.now().date()             # On récupère la date d'aujourd'hui
    today_start = datetime.combine(today, time.min)   # On vient récuperer la première date de la journée
    today_end = datetime.combine(today, time.max)     # la dernière date de la journée donc normalement 20h
    df_today = df.loc[(df['date'] >= today_start) & (df['date'] <= today_end)] 

    # Ici on fait les calculs de la variation, prix le plus bas, le plus haut, la volatilitée...
    # round() permet d'arroundir à un chiffre significatif défini. 
    variation = round((df_today['prix'].iloc[-1] - df_today['prix'].iloc[0]) / df_today['prix'].iloc[0] * 100,2)
    min_price = df_today['prix'].min()
    max_price = df_today['prix'].max()
    daily_volatility = round(df_today['prix'].std(),6)
    price_return = round((df_today['prix'].iloc[-1] - df_today['prix'].iloc[0]) / df_today['prix'].iloc[0] * 100,4)

    # On génère la avec des conteneurs html (l'interface graphique pour notre serveur)
    # lorsqu'on fait '{}' puis après '.format(variable)' la variable va se mettre dans les guillements.
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



# Meme mfonction que en haut mais cette fois sur la journée précédente
def generate_table_yesterday():
    yesterday = datetime.now().date() - timedelta(days=1)
    yesterday_start = datetime.combine(yesterday, time.min)
    yesterday_end = datetime.combine(yesterday, time.max)
    df_yesterday = df.loc[(df['date'] >= yesterday_start) & (df['date'] <= yesterday_end)]

    # De même calcul des volatilités...
    variation = round((df_yesterday['prix'].iloc[-1] - df_yesterday['prix'].iloc[0]) / df_yesterday['prix'].iloc[0] * 100,2)
    min_price = df_yesterday['prix'].min()
    max_price = df_yesterday['prix'].max()
    daily_volatility = round(df_yesterday['prix'].std(),6)
    price_return = round((df_yesterday['prix'].iloc[-1] - df_yesterday['prix'].iloc[0]) / df_yesterday['prix'].iloc[0] * 100,4)

    # La table
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


# Methode qui permet de faire la bonne méthode selon l'heure.
def get_table():
    now = datetime.now() # on récupère la date d'aujourd'hui
    today_at_8pm = datetime.combine(now.date(), time(hour=20))  # Puis la date d'aujourd'hui et l'heure de 20h
    if now.hour >= today_at_8pm.hour:  # Si on est supérieur à 20h aujourd'hui
        return generate_table()        # On fait la méthode qui génère la table d'aujourd'hui
    else:
        return generate_table_yesterday() # Si on est avant 20h, on génère la table de la journée d'hier


# Créer le tableau de bord
# https://dash.plotly.com/ml-and-ai-templates
# Voir le site pour mieux comprendre html 
# Ici le container est le bloc principal, il contient tous les autres blocs.
# Pour certains blocs, j'ai centré la variable et rajouté un contour à bord arrondi.
app = dash.Dash(__name__)
app.layout = html.Div(className='container', children=[
        html.Div(className='header', children=[
            html.Div(className='title', children=[
                html.H1(children='Tableau de bord financier : Cardano ADA/EUR', style={'text-align': 'center', 'border': '1px solid #ddd', 'border-radius': '10px'})     # Bloc pour le titre 
        ]),
        html.Div(className='subtitle', children=[
            html.H2(id='last-price', children='Dernier prix : {} €'.format(df['prix'].iloc[-1]), style={'text-align': 'center'}),               # Bloc pour le dernier prix
            html.H2(id='last-date', children='Dernière Date : {}'.format(df['date'].iloc[-1]), style={'text-align': 'center'})                  # Bloc pour la dernière date et donc voir l'actualisation
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
        ]),     # Bloc pour le graphique 
    ], style={'border': '1px solid #ddd', 'border-radius': '5px'}), # bloc qui contient le graphique aussi que les boutons pour modifier le graphique
    html.Div(className='table-container', children=get_table(), style={'border': '1px solid #ddd', 'border-radius': '10px', 'margin-top': '20px'})   # bloc qui contient le tableau d'analyse
], style={
    'margin': '0 auto',
    'max-width': '800px',
    'font-family': 'Arial, sans-serif'
})  # Un petit css pour que nos blocs soient centré au milieu de page et permet d'etre lisible pour tous appareils (ayant differentes résolutions)

# Callback pour mettre à jour le graphique en fonction de la durée sélectionnée
@app.callback(Output('graphique', 'figure'), [Input('duree', 'value')])
def update_figure(duree):
    # df.tail()  renvoie la taille donc modifie la ligne des abscisses donc la rétricie pour 1h...
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
    fig.add_trace(go.Scatter(x=df_filtre['date'], y=df_filtre['prix'], mode='lines', line=dict(color='#34A853'), fill='tonexty', fillcolor='rgba(52,168,83,0.3)'))    # ici on retrace notre le graph
    fig.update_layout(transition_duration=500, yaxis={'range': [min_price, max_price]})
    return fig

# Main
if __name__ == '__main__':
    app.run_server(host = "0.0.0.0", port = 8050, debug=True)   # on run le serveur 
