import folium
import branca
from data.coordinates_corp import corp
from data.coordinates_dormitories import dormitories

#  draw corps and add popups
#  * @param {m} folium.folium.Map example of map object
def block_a(m: folium.folium.Map):
    weight = corp["weight"]
    for i in range (len(corp["building"])):
        location = corp["building"][i]["loc"]
        color = dormitories["building"][i]["color"]
        name = corp["building"][i]["name"]
        html = f"""
            <body style=background-color:PaleTurquoise>
            <h1> <font face="impact" size="7" color="DarkBlue"> {corp["building"][i]["name"]} </font></h1>
            <p><font face="cascadia code" size="3"> {corp["building"][i]["address"]} </font></p>
            <p><font face="cascadia code" size="3"> {corp["building"][i]["info"]} </font></p>
            <img src={corp["building"][i]["img"]} width=490 height=280>
        """
        iframe = branca.element.IFrame(html=html, width='510', height='500')
        popup = folium.Popup(iframe, max_width=500)
        folium.Polygon(
            locations=location,
            color=color,
            weight=weight,
            fill_color= color,
            fill_opacity=0.3,
            fill=True,
            popup=popup,
            tooltip=name).add_to(m)

#  draw dormitories and add popups
#  * @param {m} folium.folium.Map example of map object
def block_b(m: folium.folium.Map):
    weight = dormitories["weight"]
    for j in range (len(dormitories["building"])):
        location = dormitories["building"][j]["loc"]
        color = dormitories["building"][j]["color"]
        name = dormitories["building"][j]["name"]
        html = f"""
            <body style=background-color:MistyRose>
            <h1> <font face="impact" size="7" color="RoyalBlue"> {dormitories["building"][j]["name"]} </font></h1>
            <p><font face="cascadia code" size="3"> {dormitories["building"][j]["address"]} </font></p>
            <p><font face="cascadia code" size="3"> {dormitories["building"][j]["info"]} </font></p>
            <img src={dormitories["building"][j]["img"]} width="300" height="280">
        """
        iframe = branca.element.IFrame(html=html, width='460', height='500')
        popup = folium.Popup(iframe, max_width=500)
        folium.Polygon(
            locations=location,
            color=color,
            weight=weight,
            fill_color= color,
            fill_opacity=0.3,
            fill=True,
            popup=popup,
            tooltip=name).add_to(m)
    
