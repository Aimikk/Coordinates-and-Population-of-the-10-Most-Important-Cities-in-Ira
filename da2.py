import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

# Data for the 10 most important cities in Iran
data = {
    "City": ["Tehran", "Mashhad", "Isfahan", "Karaj", "Shiraz", "Tabriz", "Qom", "Ahvaz", "Kermanshah", "Urmia"],
    "Latitude": [35.6892, 36.3264, 32.6447, 35.8272, 29.6100, 38.0814, 34.6400, 31.3047, 34.3325, 37.5439],
    "Longitude": [51.3889, 59.5433, 51.6675, 50.9489, 52.5425, 46.3006, 50.8764, 48.6783, 47.0933, 45.0647],
    "Population": [14148000, 3372090, 2219343, 1973470, 1565572, 1558693, 1201158, 1184788, 946651, 736224]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create map
plt.figure(figsize=(12, 10))
m = Basemap(projection="merc", llcrnrlat=25, urcrnrlat=40, llcrnrlon=44, urcrnrlon=63, resolution='i')

# Draw coastlines and country borders
m.drawcoastlines()
m.drawcountries()

# Plot each city
for i in range(len(df)):
    x, y = m(df["Longitude"][i], df["Latitude"][i])
    m.plot(x, y, "bo", markersize=df["Population"][i] / 1000000)
    plt.text(x, y, f"{df['City'][i]}: {df["Population"][i]}", fontsize=12, ha="right")

plt.title("Coordinates and Population of the 10 Most Important Cities in Iran")
plt.show()
