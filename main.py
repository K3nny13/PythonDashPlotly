import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv("report.csv")
x = df["Hours"]
ykva = df["Demand (kVA)"]
ykwh = df["Consumption (kWh)"]
ykw = df["Power (kW)"]

print(df.head())


app = dash.Dash()
app.layout = (html.Div([html.H1("Power Factor Graph"),
                        dcc.Graph(id="test",
                                  figure=go.Figure(
                            data=[
                                go.Scatter(x=x,
                                           y=ykva,
                                           mode='lines',
                                           name="kVA"),
                                go.Scatter(x=x,
                                           y=ykwh,
                                           mode='lines',
                                           name="kWH"),
                                go.Scatter(x=x,
                                           y=ykw,
                                           mode='lines',
                                           name="kW")                                
                                ],
                            layout=go.Layout(
                                title="Demand (kVA) Scatter Plot"
                            )))]))

if __name__ == "__main__":
    app.run_server(debug=True)


go.Figure()