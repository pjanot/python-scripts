from py2neo import neo4j
from py2neo import node, rel

graph_db = neo4j.GraphDatabaseService()

graph_db.clear()


links = [ (0, 1),
          (0, 2),
          (0, 3),					
          (0, 4),
          (0, 4), # we can have a duplicate reliationship
          (3, 4),
          (3, 5),
          (3, 6),
          (4, 5) ]

links = zip( range(0,10000), range(1,10001) )

existing_nodes = dict()

ids = graph_db.get_or_create_index( neo4j.Node, 'Ids')

for id1, id2 in links:
    print id1, id2
    node1 = ids.get_or_create( 'id', id1, {'id':id1} )
    node2 = ids.get_or_create( 'id', id2, {'id':id2} )       
    n1_n2 = graph_db.create( rel(node1, "follows", node2) )

