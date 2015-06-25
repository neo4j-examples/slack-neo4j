import requests
import os
from graph import graph

token = os.environ.get('SLACK_TOKEN')

def insert():
    # Upload Channels.
    res = requests.get("https://slack.com/api/channels.list?token={}".format(token))

    if res.status_code != 200:
        raise Exception(u"Invalid Response from Channels endpoint {}".format(res.status_code))

    channels = res.json()['channels']

    query = """
    UNWIND {channels} AS channel
    MERGE (c:Channel {id:channel.id})
    ON CREATE SET c.name = channel.name
    RETURN COUNT(channel)
    """

    channel_count = graph.cypher.execute_one(query, {'channels': channels})

    # Upload Users.
    res = requests.get('https://slack.com/api/users.list?token={}'.format(token))

    if res.status_code != 200:
        raise Exception(u"Invalid Response from Users endpoint {}".format(res.status_code))

    users = res.json()['members']

    query = """
    UNWIND {users} AS user
    MERGE (u:User {id:user.id})
    SET u.username = user.name,
        u.fullname = user.profile.real_name
    RETURN COUNT(user)
    """

    user_count = graph.cypher.execute_one(query, {'users': users})

    # Upload Memberships.
    query = """
    MERGE (channel:Channel {id: {channel_id} })
    MERGE (user:User {id: {user_id} })
    MERGE (user)-[:MEMBER_OF]->(channel)
    """

    membership_count = 0

    for channel in channels:
        channel_id = channel['id']
        users = channel['members']

        for user_id in users:
            graph.cypher.execute(query, {'channel_id':channel_id, 'user_id': user_id})
            membership_count += 1

    return "{0} channels, {1} users, and {2} memberships uploaded.".format(channel_count, user_count, membership_count)