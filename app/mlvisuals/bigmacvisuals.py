import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from app import app, BASEDIR

df = pd.read_csv(BASEDIR + "/mldata/BigMac.csv", sep = '\t')

df = df.loc[:10]

fig = plt.figure(constrained_layout=False, figsize=(24, 16))
spec = fig.add_gridspec(2, 2)
fig_ax1 = fig.add_subplot(spec[0:1,:])
fig_ax2 = fig.add_subplot(spec[1:2,:])

index = np.arange(df.shape[0])
country = df['Country']
price = df['Price']
wage = df['Wage']
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = fig_ax1.bar(x=index, height=price, width=bar_width,
                alpha=opacity, color='b',
                label='Price')
rects2 = fig_ax1.bar(x=index + bar_width, height=wage, width=bar_width,
                alpha=opacity, color='r',
                label='Wage')

fig_ax1.set_xticks(index)
fig_ax1.set_xticklabels(country)
fig_ax1.set_title("Price and Wage: Selected Countries")
fig_ax1.legend()


fig_ax2.scatter(price, wage)
plt.show()

