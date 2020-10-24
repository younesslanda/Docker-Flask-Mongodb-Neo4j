from Load import Load

if __name__ == '__main__':
    load = Load()
    load.insert_restaurant_to_graph()
    load.insert_geojson_to_mongodb()