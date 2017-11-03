from graphapi import Graph,ComplexEncoder
import json
access_token='1257032691047126|mP2cUAf8cIH-ZA0WntiqScJT8HI'
version = '2.10'
graph = Graph(access_token,version)

pages = graph.getPages('narendramodi',limit=2)

tempposts = []

for page in pages:
    for post in graph.getPosts(pageid=page.id):
        tempposts.append(post)

print json.dumps(tempposts,cls=ComplexEncoder)
