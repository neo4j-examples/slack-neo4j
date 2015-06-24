import os

import web

from slack import insert_channels, insert_users
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
            type = text.split(" ")[1]

            if type == "channels":
                channels = insert_channels()
                return "{} channels uploaded".format(channels)
            elif type == "users":
                users = insert_users()
                return "{} users uploaded.".format(users)
            else:
                return "No endpoint for inserting {} yet.".format(type)

        if command == "cypher":
            return cypher(text[7:])

        return "Unknown command: {}".format(command)
