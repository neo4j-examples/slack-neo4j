from graph import graph

def create_unique_if_doesnt_exist(label, property):
    if property not in graph.schema.get_uniqueness_constraints(label):
        try:
            graph.schema.create_uniqueness_constraint(label, property)
        except Exception as e:
            print e

def create_index_if_doesnt_exist(label, property):
    if property not in graph.schema.get_indexes(label):
        try:
            graph.schema.create_index(label, property)
        except Exception as e:
            print e

create_unique_if_doesnt_exist("User", "id")
create_unique_if_doesnt_exist("Channel", "id")

create_index_if_doesnt_exist("User", "username")
create_index_if_doesnt_exist("Channel", "name")