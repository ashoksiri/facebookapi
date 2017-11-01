from graphapi import Graph

access_token='1257032691047126|mP2cUAf8cIH-ZA0WntiqScJT8HI'
version = '2.10'
graph = Graph(access_token,version)

print graph.getpages('narendramodi',limit=100)