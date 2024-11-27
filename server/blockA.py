import folium
from coordinates import locations, locations2, locations3

def block_a(m):
    
    folium.Polygon(
        locations=locations,
        color="orange",
        weight=6,
        fill_color="orange",
        fill_opacity=0.3,
        fill=True,
        popup="Tokyo, Japan",
        tooltip="Click me!",
    ).add_to(m)

    folium.Polygon(
        locations=locations2,
        color="orange",
        weight=6,
        fill_color="orange",
        fill_opacity=0.3,
        fill=True,
        popup="Tokyo, Japan",
        tooltip="Click me!",
    ).add_to(m)

    folium.Polygon(
        locations=locations3,
        color="orange",
        weight=6,
        fill_color="orange",
        fill_opacity=0.3,
        fill=True,
        popup="Tokyo, Japan",
        tooltip="Click me!",
    ).add_to(m)
