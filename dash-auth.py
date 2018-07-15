import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

USERNAME_PASSWORD_PAIRS = [
    ['JamesBond', '007'], ['LouisArmstrong', 'satchmo']
]

app = dash.Dash()
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)

app.layout = html.Div([
    dcc.RangeSlider(
        id='range-slider',
        min=-8,
        max=8,
        marks={i: str(i) for i in range(-8, 9)},
        value=[-4, 4]
    ),
    html.H1(id='product')  # this is the output
], style={'width': '80%', 'margin': '0 auto', "textAlign": "center"})


@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
def update_value(value_list):
    return value_list[0] * value_list[1]


if __name__ == '__main__':
    app.run_server(debug=True)
