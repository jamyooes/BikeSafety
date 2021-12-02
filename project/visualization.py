#James Yoo
#https://data.cityofnewyork.us/Transportation/Bicycle-Routes/7vsa-caz7
#https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

import pandas as pd
# import folium

# m = folium.Map(location=[40.7128, -74.0060], zoom_start = 13, prefer_canvas = True)

# bikeRoutes = "Bicycle Routes.geojson"

# style = {'color': '#558800'}
# folium.GeoJson(bikeRoutes, name="geojson", style_function = lambda x: style).add_to(m)
# folium.LayerControl().add_to(m)

fatality_data = pd.read_csv("Killed.csv")
injured_data = pd.read_csv('Injured.csv')
accident_1 = pd.read_csv('BicycleAccidents.csv')
accident_1 = accident_1.dropna(subset=["LATITUDE"])
accident_2 = pd.read_csv('BicycleAccidents2.csv')
accident_2 = accident_2.dropna(subset=["LATITUDE"])
accident_3 = pd.read_csv('BicycleAccidents3.csv')
accident_3 = accident_3.dropna(subset=["LATITUDE"])
accident_4 = pd.read_csv('BicycleAccidents4.csv')
accident_4 = accident_4.dropna(subset=["LATITUDE"])
accident_5 = pd.read_csv('BicycleAccidents5.csv')
accident_5 = accident_5.dropna(subset=["LATITUDE"])
accident_6 = pd.read_csv('BicycleAccidents6.csv')
accident_6 = accident_6.dropna(subset=["LATITUDE"])
accident_7 = pd.read_csv('BicycleAccidents7.csv')
accident_7 = accident_7.dropna(subset=["LATITUDE"])
accident_8 = pd.read_csv('BicycleAccidents8.csv')
accident_8 = accident_8.dropna(subset=["LATITUDE"])
accident_9 = pd.read_csv('BicycleAccidents9.csv')
accident_9 = accident_9.dropna(subset=["LATITUDE"])
accident_10 = pd.read_csv('BicycleAccidents10.csv')
accident_10 = accident_10.dropna(subset=["LATITUDE"])
# m.save(outfile='nycMap.html')
