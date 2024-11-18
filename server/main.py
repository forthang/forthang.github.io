import folium
import requests
import logging
import xml.etree.ElementTree as ET

API = 'https://api.openstreetmap.org/'
data = '37.6173,55.7268,37.6183,55.7273'  # Bounding box

# Get XML from API
response = requests.get(API + 'api/0.6/map?bbox=' + data)

# XML parse
root = ET.fromstring(response.content)

# Create map
m = folium.Map(location=[55.7268349, 37.6173], zoom_start=25)

# Parse nodes
#/brief take points like (x,y) for creating rectangles or marking location
for node in root.findall('node'):
    lat = float(node.get('lat'))
    lon = float(node.get('lon'))
    pass

# Add a marker for the specified location
folium.Marker(
    location=[55.7268349, 37.6173],
    popup='Ленинский проспект, 6',
    icon=folium.Icon(color='red')
).add_to(m)

# Save to HTML
m.save("map.html")

# Logging
logging.basicConfig(level=logging.INFO, filename="MISSIS_Map_logs.log", filemode="w")
logging.info('Map has been saved to map.html')
logging.info('Response content:\n' + response.text)