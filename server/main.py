import folium
import logging
from blockA import block_a

# Create map
m = folium.Map(location=[55.7282903, 37.6096873], zoom_start=15)

# Parse nodes
#/brief take points like (x,y) for creating rectangles or marking location

block_a(m)

# Save to HTML
m.save("../client/public/map.html")

# Logging
logging.basicConfig(level=logging.INFO, filename="MISSIS_Map_logs.log", filemode="w")
logging.info('Map has been saved to map.html')
# logging.info('Response content:\n' + response.text)

