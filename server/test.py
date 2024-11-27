from coordinates import coordinates_of_buildings
import numpy as np

for building in coordinates_of_buildings.values():
    temp_location = []
    for coordinates in building:
        #print(coordinates.values())
        temp_location.append(coordinates.values())
    print(temp_location)
    print('new building')
