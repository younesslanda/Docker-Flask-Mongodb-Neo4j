from py2neo import Graph , Node , Relationship
from pymongo import MongoClient , GEOSPHERE
from Extract import Extract

URI_NEO4J = "bolt://neo4j-DB:7687"
USER_NEO4J = "neo4j"
PASSWORD_NEO4J = "test"

class Load:
    def __init__(self):
        self.graph = Graph(URI_NEO4J, auth=(USER_NEO4J, PASSWORD_NEO4J), encrypted=False)
        print("Connected to Neo4j !")
        self.client = MongoClient('mongo-DB', 27017)
        print("Connected to MongoDB !")
        extract = Extract()
        self.restaurant_data = extract.restaurant_data
        self.geojson_data = extract.geojson_data
        
    
    def insert_restaurant_to_graph(self):
        restaurant_data = self.restaurant_data
        graph = self.graph

        tx = graph.begin()

        for rest in restaurant_data:
            a = Node("Restaurant", name=rest['name'], latitude=rest['latitude'], longitude=rest['longitude'], address=rest['address'], phone=rest['phone'])
            b = Node("Type", type_restaurant=rest['cuisine_type'])
            ab = Relationship(a, "est_de_type", b)

            tx.merge(a, "Restaurant", "name")
            tx.merge(b, "Type", "type_restaurant")
            tx.merge(ab)
        tx.commit()

        print("Restaurant data have been inserted.")
    
    def insert_geojson_to_mongodb(self):
        geojson_data = self.geojson_data
        client = self.client

        db = client['db_cyclable']
        collection = db['collection']
        self.collection = collection

        collection.create_index([("geometry", GEOSPHERE)])
        for feature in geojson_data['features']:
            collection.insert_one(feature)
        
        print("Geojson data have been inserted.")