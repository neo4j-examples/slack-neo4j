import web
#from graph import overview
#import requests

urls = (
    '/', 'index',
    '/slack', 'slack'
)

class index:
    def GET(self):
         return "Neo4j Slack Integration"

class slack:
    def POST(self):
         print web.data()
         input = web.input()
         print input
         return "It works"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()