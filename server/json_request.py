import requests
import xml.etree.ElementTree as ET
import json

response = requests.get("https://www.openstreetmap.org/api/0.6/way/418322639")
root = ET.fromstring(response.content)
node_refs = []
coordinates = []
name = None
for element in root:
    if element.tag == "way":
        for nd in element.findall("nd"):
            ref = nd.attrib.get("ref")
            if ref:
                node_refs.append(ref)
        for tag in element.findall("tag"):
            if tag.attrib.get("k") == "name":
                name = tag.attrib.get("v")
for node_id in node_refs:
    node_response = requests.get(f"https://www.openstreetmap.org/api/0.6/node/{node_id}")
    node_root = ET.fromstring(node_response.content)
    for node in node_root.findall("node"):
        lat = node.attrib.get("lat")
        lon = node.attrib.get("lon")
        if lat and lon:
            coordinates.append((float(lat), float(lon)))
result = {
    "name": name,
    "coordinates": coordinates}
with open('output.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
