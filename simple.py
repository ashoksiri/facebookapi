from graphapi import Graph

access_token='1257032691047126|mP2cUAf8cIH-ZA0WntiqScJT8HI'
version = '2.10'
graph = Graph(access_token,version)

pages = graph.getPages('narendramodi',limit=5)

for page in pages:
    print page.id,graph.getPage(id=page.id)
