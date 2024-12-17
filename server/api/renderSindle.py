from OSMPythonTools.api import Api
from OSMPythonTools.overpass import Overpass
import folium
from pydantic import BaseModel

# Define the BuildingData class
class BuildingData(BaseModel):
    BuildingName: str
    address: str
    info: str
    color: str
    img: str
    html: str

def render_single(data: BuildingData) -> str:
    name = data.BuildingName
    address = data.address
    info = data.info
    color = data.color
    img = data.img
    html = data.html
    m = folium.Map(location=    [55.7227456, 37.6198714], zoom_start=15)
    m.save(f"../../client/public/map-new-item.html")
    return "test"
    #
    # overpass = Overpass()
    #
    # try:
    #     parts = address.split()
    #     house_number = parts[-1]
    #     street_name = ' '.join(parts[:-1])
    #
    #     street_name = street_name.strip()
    #     house_number = house_number.strip()
    #
    #     if not house_number.isdigit():
    #         print("House number should be a valid number.")
    #         return ""
    #
    # except Exception as e:
    #     print(f"Error processing address: {e}")
    #     return ""
    #
    # query = f"""
    # [out:json];
    # way["building"]["addr:street"="{street_name}"]["addr:housenumber"="{house_number}"];
    # out body;
    # >;
    # out skel qt;
    # """
    #
    # print("Generated Query:", query)
    #
    # try:
    #     result = overpass.query(query)
    #
    #     if not result.elements():
    #         print("No results found for the specified address.")
    #         return ""
    #
    #     building = result.elements()[0]
    #     lat_lon_coords = [(node.lat(), node.lon()) for node in building.nodes()]
    #
    #     # Save map to ../../client/public
    #     m = folium.Map(location=lat_lon_coords[0], zoom_start=15)
    #     folium.Polygon(
    #         locations=lat_lon_coords,
    #         color=color,
    #         fill=True,
    #         fill_opacity=0.5,
    #         popup=folium.Popup(html or f"<strong>{name}</strong><br>{info}", max_width=300)
    #     ).add_to(m)
    #
    #     # Save map with path adjustment
    #     m.save(f"../../client/public/{name.replace(' ', '_')}_map.html")
    #     return name  # Return the building name
    #
    # except Exception as e:
    #     print(f"An error occurred while querying Overpass API: {e}")
    #     return ""

