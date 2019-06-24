import pandas as pd
import matplotlib.pyplot as plt
import time
df = pd.read_csv("/home/kamikaze/forecasting/AQI_with_mean.csv")
df.index = df['timestamp'].apply(pd.Timestamp)
del df['timestamp']
plt.figure()
df.plot()
plt.legend(loc= 'best')
plt.show()
#The output is 2 graphs, figure out why.. Also split the graphs day wise. Plot them one underneath the other and try to see a pattern.