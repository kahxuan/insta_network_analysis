import json
import random
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from util import plot_network

app = dash.Dash(__name__)
server = app.server
app.title = 'Instagram Network Visualisation'

with open('result1.json') as f:
    res1 = json.load(f)

with open('result2.json') as f:
    res2 = json.load(f)

seed = random.randint(1, 100)

app.layout = html.Div(children=[

    html.H2(children='My Instagram Network', 
        className='header-div'),

    html.Div(
        html.A("@k_xuanlim", href='http://instagram.com/k_xuanlim/', target="_blank"), 
        className='header-div'),
    html.Div(
        html.A("View my code", href='https://github.com/kahxuan/insta_clustering', target="_blank"), 
        className='header-div'),
    
    

    html.Div([
            html.Span('Click and drag to zoom in, double click to rescale. On the legend, click to hide a cluster, double click to show only one specific cluster.', className='graph-desc'),
            html.Div(
                dcc.Graph(
                    id='network-graph1',
                    style={'height': 500},
                    figure=plot_network(np.array(res1['adjacencym']), 
                        res1['clusters'], 
                        res1['cluster_names'], 
                        {int(key): value for key, value in res1['id_to_name'].items()}, 
                        seed)
                    ),
                className='graph-div')],
        className='graph-block'
    ),


    html.Div([
        html.Span('Users grouped into smaller clusters by decreasing threshold for cluster splitting.', className='graph-desc'),
        html.Div(
            dcc.Graph(
                id='network-graph2',
                style={'height': 500},
                figure=plot_network(np.array(res2['adjacencym']), 
                    res2['clusters'], 
                    res2['cluster_names'], 
                    {int(key): value for key, value in res2['id_to_name'].items()}, 
                    seed)
                ),
            className='graph-div')],
        className='graph-block'
    ),

    html.Div(children='* Usernames in the network are masked with randomly generated string',
        className='footer-div'),
])

if __name__ == '__main__':
    app.run_server(debug=True)