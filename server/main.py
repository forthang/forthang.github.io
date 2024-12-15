import folium
import logging
from blockA import block_a
from blockA import block_b

# Creating init map
def create_base_map(x: float, y: float, z: int) -> folium.folium.Map:
    return folium.Map(location=[x, y], zoom_start=z)

#/brief creating map with corps
# vars: x - start lon
#       y - start lat
#       z - start zoom

def generate_block_a_map():
    x = float(55.7282903)
    y = float(37.6096873)
    z = int(16)
    block_a_map: folium.folium.Map = create_base_map(x, y, z)
    block_a(block_a_map)
    block_a_map.save("../client/public/map-block-a.html")
    logging.info("Map for Block A has been saved to map-block-a.html")

def generate_block_b_map():
    x = float(55.67855)
    y = float(37.56294)
    z = int(13)
    block_b_map: folium.folium.Map = create_base_map(x, y, z)
    block_b(block_b_map)
    block_b_map.save("../client/public/map-block-b.html")
    logging.info("Map for Block B has been saved to map-block-b.html")


m = folium.Map(location=[55.7282903, 37.6096873], zoom_start=16)
m.save("../client/public/map.html")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="MISSIS_Map_logs.log", filemode="w")
    generate_block_a_map()
    generate_block_b_map()
    logging.info("All maps generated successfully.")
