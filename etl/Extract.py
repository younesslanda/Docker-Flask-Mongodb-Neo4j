import json

path_json = '/data/data1.json'
path_geojson = '/data/reseau_cyclable_montreal.geojson'

class Extract:
    def __init__(self):
        self.restaurant_data = json.load(open(path_json))
        self.geojson_data = json.load(open(path_geojson))
        print("Data have been successfully extracted.")