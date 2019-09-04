import numpy as np
import pandas as pd
import scipy as sp
import scipy.integrate as spi
import dash
import dash_core_components as dcc
import dash_html_components as html

accelerometer_df = pd.read_csv("data/Driving - Recording 1.csv")

vel = spi.cumtrapz(accelerometer_df.AccY, x=accelerometer_df.timestamp)
print(vel)

