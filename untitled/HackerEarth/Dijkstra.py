
import sys

def dijkstra(g, start_node):




N_nodes = int(input())
N_edges = int(input())

visited = [False for i in range(N_edges+1)]
distance = [sys.maxsize for i in range(N_edges+1)]
graph = [[] for i in range(N_edges + 1)]

for i in range(N_edges):
    e1, e2, w = [int(x) for x in input().split()]

    graph[e1].append((e2, w))

    graph[e2].append((e1, w))

print(graph)
