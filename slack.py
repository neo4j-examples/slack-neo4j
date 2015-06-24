import requests
import json
import os
from py2neo import Graph

url = os.environ.get('NEO4J_URL',"http://localhost:7474/db/data")
token = os.environ.get('SLACK_TOKEN')
graph = Graph(url)

def insert() :
# request from slack
    res = requests.get("https://slack.com/api/channels.list?token="+token)    
    if res.status_code != 200: 
        raise Exception("Invalid Response from Channels endpoint "+res.status_code)
    channels = res.json()['channels']
    query = """
       unwind {channels} as channel
       merge (c:Channel {id:channel.id}) ON CREATE SET c.name = channel.name
    """
    graph.cypher.execute(query, channels)
    

if __name__ == "__main__":
    print insert()
