import folium
import requests
import logging
import xml.etree.ElementTree as ET

API = 'https://api.openstreetmap.org/'
data = '15,15,15,15'

#get xml from api
response = requests.get(API + 'api/0.6/map?bbox=' + data)

#xml parse
root = ET.fromstring(response.content)

#create map
m = folium.Map(location=[55.7268349, 37.6059714], zoom_start=25)

#parse nodes
#lat - latitude, lon-longitude
for node in root.findall('node'):
    lat = float(node.get('lat'))
    lon = float(node.get('lon'))
    folium.Marker(location=[lat, lon]).add_to(m)

#to html
m.save("map.html")

#logging
logging.basicConfig(level=logging.INFO, filename="MISSIS_Map_logs.log",filemode="w")
logging.info('Map has been saved to map.html')

