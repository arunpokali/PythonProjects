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
    # distance[source][destination][0] => distance
    # distance[source][destination][1] => path

    distance = [ [ [10**7 + 9,[]] for _ in range(n+1) ] for _ in range(n+1)]

    # for i in distance:
    #      print(i)

    visited = [[False] * (n+1) for _ in range(n+1)]

    for s_val in range(n):
        #visited = [False] * (n+1)
        source = s_val + 1
        distance[source][source][0] = 0
        distance[source][source][1] += [source]


        que = [source]

        while que :
            node = que.pop(0)

            if not visited[source][node]:


                for node_val in graph[node]:
                    #distance[source][node_val][0] = min(distance[source][node_val][0], 1 + distance[source][node][0])
                    if distance[source][node_val][0] > 1 + distance[source][node][0] :
                        distance[source][node_val][0] = 1 + distance[source][node][0]
                        distance[source][node_val][1] += [node_val]+distance[source][node][1]

                    #distance[source][node_val][1].append(source)
                    que.append(node_val)

                visited[source][node] = True

    return distance

# print(graph)
node_dist = short_path(graph,cap_city,n)


# for i in node_dist:
#     print(i)
# print(node_dist[3][5], node_dist[5][3])


queries = int(input())

for _ in range(queries):
    a, p = [int(x) for x in input().split()]
    p_node_list =[]
    for i, val in enumerate(product):
        if val == p:
            p_node_list.append(i)

    city_list = []
    print("chef's city : ", a)
    print("product city list : ", p, p_node_list, sep=" ")
    for p_node in p_node_list:
        path = node_dist[a][p_node][1]
        min_v = []
        print("path", " ", path)
        for n_val in path:
            min_v.append((n_val, node_dist[cap_city][n_val][0]))

        print("min_v :", " ", min_v)
        city_list.append(max(min_v, key = lambda d: (d[1])))
        print("city : ", city_list, sep=" ")

    print("city_list",city_list, sep=" ")
    p_city = sorted(city_list, reverse=True, key = lambda d: (d[1], d[0]))
    print(p_city[0][0])

