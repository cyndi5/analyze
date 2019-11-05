import numpy as np
from scipy import signal, optimize, stats, integrate, mean
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

import argparse

parser = argparse.ArgumentParser(description='Uses Plotly Dash core to plot a CSV from Google Science Journal accelerometer readings.')
parser.add_argument("--file", required=True, default=None, type=str, help="path to CSV")

args = parser.parse_args()

accelerometer_df = pd.read_csv(args.file)
print(accelerometer_df.head(5))
AccY = accelerometer_df.AccY - np.mean(accelerometer_df.AccY)
timestamp = np.subtract(accelerometer_df.timestamp, accelerometer_df.timestamp[0]) / 1000.0
vel = (integrate.cumtrapz(AccY, timestamp) * 3600 / 1000).clip(0)
print(vel)

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Google Science Accelerometer Recording Analysis'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': timestamp, 'y': AccY, 'type': 'line', 'name': 'AccY (m/s/s)'},
                {'x': timestamp, 'y': vel, 'type': 'line', 'name': 'Vel (km/h)'},
            ],
            'layout': {
                'title': 'Velocity and Acceleration of Automobile over Time'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
