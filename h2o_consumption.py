"""
Read csv file from URL and display bar chart.
Created: 2019-09-15
"""

import matplotlib.pyplot as plt
import pandas as pd
import requests
import sys

url = "https://raw.githubusercontent.com/SF19PB1-hardeep-leyl/water_nyc/water_consumption_in_nyc.csv.csv"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as error:
    print(error, file = sys.stderr)

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
