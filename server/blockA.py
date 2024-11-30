import folium
from coordinates_corp import corp
from coordinates_dormitories import dormitories

def block_a(m):
    color = corp["color"]
    weight = corp["weight"]
    for i in range (len(corp["building"]]
        locat = corp["building"][index]["loc"]
        name = corp["building"][index]["name"]
        folium.Polygon(
            locations=locat,
            color=color,
            weight=weight,
            fill_color= color,
            fill_opacity=1,
            fill=True,
            popup=name)

def block_b(m):
    color = dormitories["color"]
    weight = dormitories["weight"]
    for i in range (len(dormitories["building"]]
        locat = dormitories["building"][index]["loc"]
        name = dormitories["building"][index]["name"]
        folium.Polygon(
            locations=locat,
            color=color,
            weight=weight,
            fill_color= color,
            fill_opacity=1,
            fill=True,
            popup=name)
    
