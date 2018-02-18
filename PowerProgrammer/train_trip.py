from collections import defaultdict


def solve():

    def bfs(graph, start, end):

        que = [[start]]
        c = 0
        while que:
            #print("que: ", que)
            path = que.pop(0)

            node = path[-1]

            if node == end:
                return path

            for adj in graph.get(node, []):
                t_path = list(path)
                t_path.append(adj)
                #print(adj, t_path)
                que.append(t_path)
            # c += 1
            # if c == 5:
            #     break

    nodes = int(input())

    a, b, c = [int(x) for x in input().split()]

    start_nodes = [int(x) for x in input().split()]

    graph = defaultdict(lambda: [])

    for i in range(nodes - 1):
        m, n = [int(x) for x in input().split()]
        graph[m].append(n)
        graph[n].append(m)


    paths = []
    for j in start_nodes:
        paths.append(bfs(graph, j, 1))


    cost_dict = defaultdict(lambda: {})

    for val in paths:
        for k, v in enumerate(val):
            if v != 1:
                if val[k+1] in cost_dict[v].keys():
                    cost_dict[v][val[k+1]] += 1
                else:
                    cost_dict[v][val[k+1]] = 1


    #print(cost_dict)
    cost = 0
    for val in cost_dict.values():
        for v in val.values():
            if v == 1:
                cost += a
            if v == 2:
                cost += b
            if v == 3:
                cost += c

    print(cost)

for _ in range(int(input())):
    solve()