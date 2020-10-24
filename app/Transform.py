from py2neo import Graph
from pymongo import MongoClient

URI_NEO4J = "bolt://neo4j-DB:7687"
USER_NEO4J = "neo4j"
PASSWORD_NEO4J = "test"

class Transform:
    def __init__(self):
        self.graph = Graph(URI_NEO4J, auth=(USER_NEO4J, PASSWORD_NEO4J), encrypted=False)
        self.client = MongoClient('mongo-DB', 27017)
        
        db = self.client['db_cyclable']
        collection = db['collection']
        self.collection = collection

    def get_nbRestaurants(self):
        graph = self.graph
        query = "MATCH (r:Restaurant) RETURN count(r) AS nbRestaurants"
        result = graph.run(query).data()
        self.nbRestaurants = result[0]
        return self.nbRestaurants
    
    def get_nbRestaurants_type(self):
        graph = self.graph
        query = "match (r:Restaurant)-[:est_de_type]->(t:Type) return t.type_restaurant as type , count(r) as count"
        result = graph.run(query).data()
        d = {}
        d['restaurants'] = {}
        dd = {}
        for x in result:
            dd[x['type']] = x['count']
        d['restaurants'] = dd
        self.nbRestaurants_type = d
        return self.nbRestaurants_type
    
    def get_nbSegments(self):
        collection = self.collection
        nbSegments = collection.count_documents({})
        self.nbSegments = nbSegments
        return self.nbSegments

    def get_longueurCyclable(self):
        collection = self.collection
        longueurCyclable=0

        for doc in collection.find({}):
            longueurCyclable += doc['properties']['LONGUEUR']
        
        self.longueurCyclable = longueurCyclable * 0.001
        return self.longueurCyclable