import json
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from util import plot_network

app = dash.Dash(__name__)
server = app.server
app.title = 'Instagram Network Visualisation'

with open('result.json') as f:
    res = json.load(f)

id_to_name = {int(key): value for key, value in res['id_to_name'].items()}

app.layout = html.Div(children=[

    html.H2(children='My Instagram Network'),

    html.Div(html.A("View my code", href='https://github.com/kahxuan/insta_clustering', target="_blank")),
    html.Div(html.A("Visit my Instagram", href='http://instagram.com/k_xuanlim/', target="_blank")),

    dcc.Graph(
        id='network-graph',
        style={'height': 600},
        figure=plot_network(np.array(res['adjacencym']), 
            res['clusters'], 
            res['cluster_names'], 
            id_to_name, 
            res['my_username'])
    ),

    html.Div(children='* Usernames in the network are masked with randomly generated string'),
])

if __name__ == '__main__':
    app.run_server(debug=True)