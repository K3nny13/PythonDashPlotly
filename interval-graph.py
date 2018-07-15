import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import requests

app = dash.Dash()
data_url = 'https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1' \
           '&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1'


app.layout = html.Div([
                        html.Div([
                            html.Iframe(src="https://www.flightradar24.com",
                                        height=500,
                                        width=1200)
                        ]),
                        html.Div([
                            html.Pre(id='counter_text',
                                     children="Active Flights Worldwide"),
                            dcc.Interval(id='interval-components',
                                         interval=100000,
                                         n_intervals=0)
                        ])
])


@app.callback(Output('counter_text', 'children'),
              [Input('interval-components', 'n_intervals')])
def update_layout(n):
    res = requests.get(data_url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data['stats']['total']:
        counter += data['stats']['total'][element]
    return "Active Flights Worldwide: {}".format(counter)


if __name__ == '__main__':
    app.run_server(debug=True)

