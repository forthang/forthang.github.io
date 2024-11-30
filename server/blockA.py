import folium
from coordinates_corp import corp
from coordinates_dormitories import dormitories

def block_a(m):
    color = corp["color"]
    weight = corp["weight"]
    for i in range (len(corp["building"])):
        locat = corp["building"][i]["loc"]
        name = corp["building"][i]["name"]
        folium.Polygon(
            locations=locat,
            color=color,
            weight=weight,
            fill_color= color,
            fill_opacity=0.3,
            fill=True,
            tooltip=name).add_to(m)

def block_b(m):
    color = dormitories["color"]
    weight = dormitories["weight"]
    for j in range (len(dormitories["building"])):
        locat = dormitories["building"][j]["loc"]
        name = dormitories["building"][j]["name"]
        folium.Polygon(
            locations=locat,
            color=color,
            weight=weight,
            fill_color= color,
            fill_opacity=0.3,
            fill=True,
            tooltip=name).add_to(m)
    
