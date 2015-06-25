import os

import web

from slack import insert
from graph import overview
from graph import cypher


team = os.environ.get('TEAM_TOKEN')

web.config.debug = False

urls = (
    '/', 'index',
    '/slack', 'slack'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return "Neo4j Slack Integration"


class slack:
    def POST(self):
        data = web.input()
        token = data["token"]
        if team != token:
            return "Invalid team token."

        text = data["text"]
        command = text.split(" ")[0]

        if command == "":
            return "\n" + overview()

        if command == "import":
            return insert()

        if command == "cypher":
            return cypher(text[7:])

        return "Unknown command: {}".format(command)
