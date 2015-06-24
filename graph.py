import requests
import os
import time
from py2neo import Graph

# Connect to graph and add constraints.
url = os.environ.get('NEO4J_URL',"http://localhost:7474/db/data/")
# url = "http://localhost:7474/db/data/"
graph = Graph(url)


def init():
    # Add uniqueness constraints.
    graph.cypher.execute("CREATE CONSTRAINT ON (c:Channel) ASSERT t.id IS UNIQUE;")
    graph.cypher.execute("CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE;")
    graph.cypher.execute("CREATE INDEX ON :User(name);")
    graph.cypher.execute("CREATE INDEX ON :Channel(name);")
        

def overview():
    query = """
    MATCH (c:Channel)-[r]-() 
    RETURN c.name, type(r), count(*)
    """
    rows = graph.cypher.execute(query)
    return json.dumps(rows)
