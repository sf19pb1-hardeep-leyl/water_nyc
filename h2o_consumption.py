"""
Read water consumption rates from URL and display bar chart.
"""

import matplotlib.pyplot as plt
import pandas as pd
import sys

url = "https://data.cityofnewyork.us/Environment/Water-Consumption-In-The-New-York-City/ia2d-e54m/data"

df = pd.read_csv(url, index_col=0)

fig = plt.figure() 

plt.title('NYC Water Consumption Rates')

ax = fig.add_subplot(111) 
ax2 = ax.twinx() 

width = 0.3

df.population.plot(kind='bar', color='crimson', ax=ax, width=width, position=2)
df.consumption.plot(kind='bar', color='navy', ax=ax2, width=width, position=1)
df.percapita.plot(kind='bar', color='green', ax=ax3, width=width, position=0)

ax.set_ylabel('Population')
ax2.set_ylabel('Water Consumption')
ax3.set_ylabel('Per Capita')

plt.ticklabel_format(style='plain', axis='y')

plt.show()

sys.exit(0)
