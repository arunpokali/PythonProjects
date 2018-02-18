from collections import defaultdict

from bisect import bisect_left

def primes_upto(n):

    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def binary_search(arr, x, lo=0, hi=None):

    hi = hi if hi is not None else len(arr)
    pos = bisect_left(arr, x, lo, hi)
    return pos if pos != hi and arr[pos] == x else -1

# a generator function to find all simple paths between two nodes in a
# graph, represented as a dictionary that maps nodes to their neighbors
def find_simple_paths(graph, start, end):
    visited = set()
    visited.add(start)

    nodestack = list()
    indexstack = list()
    current = start
    i = 0

    while True:
        # get a list of the neighbors of the current node
        neighbors = graph[current]

        # find the next unvisited neighbor of this node, if any
        while i < len(neighbors) and neighbors[i] in visited:
            i += 1

        if i >= len(neighbors):
            # we've reached the last neighbor of this node, backtrack
            visited.remove(current)
            if len(nodestack) < 1: break  # can't backtrack, stop!
            current = nodestack.pop()
            i = indexstack.pop()
        elif neighbors[i] == end:
            # yay, we found the target node! let the caller process the path
            yield nodestack + [current, end]
            i += 1
        else:
            # push current node and index onto stacks, switch to neighbor
            nodestack.append(current)
            indexstack.append(i + 1)
            visited.add(neighbors[i])
            current = neighbors[i]
            i = 0


# test graph:
#     ,---B---.
#     A   |   D
#     `---C---'
"""
 graph = {
    "A": ("B",),
    "B": ("A", "C", "D"),
    "C": ("B", ),
    "D": ("B",),
}
"""

Node_graph = int(input())
graph = defaultdict(lambda : [])

for _ in range(Node_graph-1):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)


tc = int(input())
prime_list = primes_upto(1000000)

while tc:
    s, e = [int(x) for x in input().split()]
    count = 0
    for path in find_simple_paths(graph, s, e):
        for num in path:
            if binary_search(prime_list, num) != -1:
                count += 1

    print(count)
    tc -= 1

