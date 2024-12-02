import folium
import logging
from blockA import block_a
from blockA import block_b

def create_base_map():
    return folium.Map(location=[55.7282903, 37.6096873], zoom_start=16)


def generate_block_a_map():
    m = create_base_map()
    block_a(m)
    m.save("../client/public/map-block-a.html")
    logging.info("Map for Block A has been saved to map-block-a.html")

def generate_block_b_map():
    m = create_base_map()
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