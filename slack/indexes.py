from graph import graph

def create_constraint(label, property):
    graph.cypher.execute("CREATE CONSTRAINT ON (n:{0}) ASSERT n.{1} IS UNIQUE".format(label, property))

def create_index(label, property):
    graph.cypher.execute("CREATE INDEX ON :{0}({1})".format(label, property))

create_constraint("User", "id")
create_constraint("Channel", "id")
create_index("User", "username")
create_index("Channel", "name")