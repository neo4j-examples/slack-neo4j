import web
#from graph import overview
#import requests

web.config.debug=False

urls = (
    '/', 'index',
    '/slack', 'slack'
)

class index:
    def GET(self):
         return "Neo4j Slack Integration"

class slack:
    def POST(self):
         data=web.input()
         text = data["text"]
         print "text "+text
         command = text.split(" ")[0]
         if (command == "") return  overview()
         if (command == "import") return insert()
         if (command == "cypher") return cypher(text[7:])
         return "It works: command: "+command

def overview():
    return "overview"

def cypher(query):
    return "cypher "+query
    
def insert():
    return "Inserting data"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
