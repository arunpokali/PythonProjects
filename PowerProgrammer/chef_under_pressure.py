from collections import defaultdict

n, k = [int(x) for x in input().split()]
cap_city = int(input())

graph = defaultdict(lambda: [])

for _ in range(n - 1):
    p, q = [int(x) for x in input().split()]
    graph[p].append(q)
    graph[q].append(p)

product = [None]

for _ in range(n):
    product.append(int(input()))


def short_path(graph, cap_city, n):

    distance = [[10**7 + 9] * (n+1) for _ in range(n+1)]
    visited = [[False] * (n+1) for _ in range(n+1)]

    for s_val in range(n):
        #visited = [False] * (n+1)
        source = s_val + 1
        distance[source][source] = 0


        que = [source]

        while que :
            node = que.pop(0)

            if not visited[source][node]:

                for node_val in graph[node]:
                    distance[source][node_val] = min(distance[source][node_val], 1 + distance[source][node])
                    #distance[node_val][source] = distance[source][node_val]
                    que.append(node_val)

                visited[source][node] = True

    return distance

# print(graph)
node_dist = short_path(graph,cap_city,n)
# for i in node_dist:
#     print(i)
#
# print(node_dist[3][5], node_dist[5][3])

queries = int(input())

for _ in range(queries):
    a, p = [int(x) for x in input().split()]
    p_node_list =[]
    for i, val in enumerate(product):
        if val == p:
            p_node_list.append(i)

    city_list = []
    for p_node in p_node_list:
        dis = node_dist[a][p_node]
        city_list.append((p_node,dis))
    #print(city_list)
    p_city = sorted(city_list, reverse=True, key = lambda d: (d[1], d[0]))
    print(p_city)

