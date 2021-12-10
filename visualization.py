#James Yoo
#Idea of the project is to display biker accidents on a web map followed with charts
#that display accidents by years
#Data sources below
#https://data.cityofnewyork.us/Transportation/Bicycle-Routes/7vsa-caz7
#https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95
#URL = https://jamyooes.github.io/BikeSafety/index.html

import pandas as pd
import folium
from datetime import datetime
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt

#Generate a map with basic start coordinates, zoom level, and prefer_canvas to reduce overall lag
m = folium.Map(location=[40.7128, -74.0060], zoom_start = 13, max_zoom = 20, prefer_canvas = True)

#This is a local file in the directory that will be used to map out the bike routes
bikeRoutes = "Bicycle Routes.geojson"

#This is the styling used for the bike routes
style = {'color': '#558800'}
folium.GeoJson(bikeRoutes, name="geojson", style_function = lambda x: style).add_to(m)

#Note that all data is filtered out from NYC Open Data because 
# the original file souorce had approximately 7 million data points
# and my machine would not cooperate, so I split the data up into pieces

#Load and reading data
#The data below all are filtered out under different parameters and will be cleaned 
#if there's no actual coordinate
fatality_data = pd.read_csv("Killed.csv")
fatality_data = fatality_data.dropna(subset=["LATITUDE"])
injured_data = pd.read_csv('Injured.csv')
injured_data = injured_data.dropna(subset=["LATITUDE"])
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

# print (len(accident_1.columns))
# print (len(accident_2.columns))

#Combine all the data
df = pd.concat([accident_1, accident_2, accident_3, accident_4, accident_5, accident_6, accident_7, accident_8, accident_9, accident_10, fatality_data, injured_data])
#remove all duplicate data values
df = df.drop_duplicates(keep='first')

#get fatality data
fatal_bike = df[df["NUMBER OF CYCLIST KILLED"] > 0]
injured_bike = df[df["NUMBER OF CYCLIST INJURED"] > 0]
df = df[df["NUMBER OF CYCLIST KILLED"] == 0]


#For charts
df3 = df
df3["CRASH DATE"] = pd.to_datetime(df3["CRASH DATE"])
df3 = df3.sort_values(by='CRASH DATE')
accidentDF = df3.groupby('CRASH DATE').count()['CRASH TIME'].transpose()
df3.set_index('CRASH DATE',inplace=True)


#2012
ts2012 = pd.Series(accidentDF, index=pd.date_range("7/1/2012", "12/31/2012"))
plt.title("2012 Accidents involving Bicycles") 
ts2012.plot()
plt.savefig('2012')
#2013
plt.clf()
ts2013 = pd.Series(accidentDF, index=pd.date_range("1/1/2013", "12/31/2013"))
plt.title("2013 Accidents involving Bicycles") 
ts2013.plot()
plt.savefig('2013')
#2014
plt.clf()
ts2014 = pd.Series(accidentDF, index=pd.date_range("1/1/2014", "12/31/2014"))
plt.title("2014 Accidents involving Bicycles") 
ts2014.plot()
plt.savefig('2014')
#2015
plt.clf()
ts2015 = pd.Series(accidentDF, index=pd.date_range("1/1/2015", "12/31/2015"))
plt.title("2015 Accidents involving Bicycles") 
ts2015.plot()
plt.savefig('2015')
#2016
plt.clf()
ts2016 = pd.Series(accidentDF, index=pd.date_range("1/1/2016", "12/31/2016"))
plt.title("2016 Accidents involving Bicycles") 
ts2016.plot()
plt.savefig('2016')
#2017
plt.clf()
ts2017 = pd.Series(accidentDF, index=pd.date_range("1/1/2017", "12/31/2017"))
plt.title("2017 Accidents involving Bicycles") 
ts2017.plot()
plt.savefig('2017')
#2018
plt.clf()
ts2018 = pd.Series(accidentDF, index=pd.date_range("1/1/2018", "12/31/2018"))
plt.title("2018 Accidents involving Bicycles") 
ts2018.plot()
plt.savefig('2018')
#2019
plt.clf()
ts2019 = pd.Series(accidentDF, index=pd.date_range("1/1/2019", "12/31/2019"))
plt.title("2019 Accidents involving Bicycles") 
ts2019.plot()
plt.savefig('2019')
#2020
plt.clf()
ts2020 = pd.Series(accidentDF, index=pd.date_range("1/1/2020", "12/31/2020"))
plt.title("2020 Accidents involving Bicycles") 
ts2020.plot()
plt.savefig('2020')
#2021
plt.clf()
ts2021 = pd.Series(accidentDF, index=pd.date_range("1/1/2021", "12/31/2021"))
plt.title("2014 Accidents involving Bicycles") 
ts2021.plot()
plt.savefig('2021')

#chart on time of accidents
df2 = df
df2["CRASH TIME"] = pd.to_datetime(df2['CRASH TIME'])
df2["CRASH TIME"] = df2['CRASH TIME'].dt.time
df2 = df2.sort_values(by='CRASH TIME')
accidentDF = df2.groupby('CRASH TIME').count()['CRASH DATE'].transpose()

df2.set_index('CRASH TIME',inplace=True)
plt.clf()
times_accident = pd.Series(accidentDF)
plt.title("Accidents involving Bicycles by time 2012-2021") 
times_accident.plot()
plt.savefig('time')

#dataframes and folium/leaflet could not work together for some reason with my dataset, so I decidedd to put everything as an array
fatal_bike = fatal_bike.values.tolist()
injured_bike = injured_bike.values.tolist()

#The important data will be the crash date index(0), crash time (1), borough (2), zip code(3), 
#Latitude (4), Longitude (5), Person injured (10) ....  
#There's tens of thousands injured cyclists so I used marker cluster, which is a plugin
mc = MarkerCluster(name = "Marker Cluster")

#map out injured data
for i in injured_bike:
    times = datetime.strptime(i[1], "%H:%M")
    times = times.strftime("%I:%M %p")
    folium.CircleMarker(location=[i[4], i[5]],
                        popup = f"Crash Date: {i[0]} Crash Time: {times}",
                        radius=1,
                        color="orange", 
                        weight=5).add_to(mc)

#add marker cluster for injured cyclist to the map
mc.add_to(m)

# map out the fatality data
for i in fatal_bike:
    times = datetime.strptime(i[1], "%H:%M")
    times = times.strftime("%I:%M %p")
    folium.CircleMarker(location=[i[4], i[5]],
                        popup = f"Crash Date: {i[0]} Crash Time: {times}",
                        radius=2,
                        color="red", 
                        weight=5).add_to(m)
#this will be used for the output
m.save(outfile='index.html')
