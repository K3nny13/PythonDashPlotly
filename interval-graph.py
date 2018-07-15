import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests

app = dash.Dash()
data_url = 'https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1' \
           '&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1'


app.layout = html.Div([
                        html.Div([
                            html.H1(id='counter_text',
                                    style={'textAlign': 'center'}),
                            dcc.Graph(id='live-update-graph',
                                      style={'width': 1800}),
                            dcc.Interval(id='interval-components',
                                         interval=3000,
                                         n_intervals=0)
                        ])
])

counter_list = []


@app.callback(Output('counter_text', 'children'),
              [Input('interval-components', 'n_intervals')])
def update_layout(n):
    res = requests.get(data_url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data['stats']['total']:
        counter += data['stats']['total'][element]
    counter_list.append(counter)
    return "Active Flights Worldwide: {}".format(counter)


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-components', 'n_intervals')])
def update_graph(n):
    fig = go.Figure(data=[
                    go.Scatter(x=list(range(len(counter_list))),
                               y=counter_list,
                               mode='lines+markers')
                    ])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

