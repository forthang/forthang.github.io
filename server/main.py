import folium
import logging
from blockA import block_a
from blockA import block_b

def create_base_map(x, y, z):
    return folium.Map(location=[x, y], zoom_start=z)


def generate_block_a_map():
    x = 55.7282903
    y = 37.6096873
    z = 16
    m = create_base_map(x, y, z)
    block_a(m)
    m.save("../client/public/map-block-a.html")
    logging.info("Map for Block A has been saved to map-block-a.html")

def generate_block_b_map():
    x = 55.67855
    y = 37.56294
    z = 12.75
    m = create_base_map(x, y, z)
    block_b(m)
    m.save("../client/public/map-block-b.html")
    logging.info("Map for Block B has been saved to map-block-b.html")

m = folium.Map(location=[55.7282903, 37.6096873], zoom_start=16)
m.save("../client/public/map.html")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="MISSIS_Map_logs.log", filemode="w")
    generate_block_a_map()
    generate_block_b_map()
    logging.info("All maps generated successfully.")
