"""

import matplotlib.pyplot as plt
import pandas as pd
import sys

url = "https://data.cityofnewyork.us/api/views/ia2d-e54m/rows.csv"

try:
    df = pd.read_csv(url, index_col = 0)
except BaseException as error:
    print(error, file = sys.stderr)
    sys.exit(1)

figure, ax0 = plt.subplots(figsize = (10, 6))
ax1 = ax0.twinx()
ax2 = ax0.twinx()
figure.canvas.set_window_title("Water Consumption")
plt.title("NYC Water Consumption Rates")

fields = [
    [2, ax0, "crimson", "Population",        "New York City Population"],
    [1, ax1, "navy",    "Water Consumption", "NYC Consumption(Million gallons per day)"],
    [0, ax2, "green",   "Per Capita",        "Per Capita(Gallons per person per day)"]
]

for field in fields:
    ax = field[1]
    color = field[2]
    series = df[field[4]]   #series is a pandas Series object.  See Series.

    series.plot(
        kind = "bar",
        color = color,
        ax = ax,
        width = .25,
        position = field[0] -.5
    )

    ax.set_ylabel(field[3], color = color)
    ax.tick_params(axis = "y", labelcolor = color)

plt.ticklabel_format(style = "plain", axis = "y")
plt.show()
