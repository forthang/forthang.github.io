import folium


def block_a(m, data):
    color = data["color"]
    loc = data["loc"]
    weight = data["weight"]
    name = data["building"]["name"]
    folium.Polygon(
        locations=loc,
        color=color,
        weight=weight,
        fill_color= color,
        fill_opacity=1,
        fill=True,
        popup=name)
    
