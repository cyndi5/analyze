import numpy as np
import pandas as pd
import scipy as sp

accelerometer_df = pd.read_csv("data/Driving - Recording 1.csv")
print(accelerometer_df.head(5))
print(accelerometer_df.timestamp)
print(accelerometer_df.AccY)
vel = np.trapz(accelerometer_df.AccY, accelerometer_df.timestamp)
print(vel)
