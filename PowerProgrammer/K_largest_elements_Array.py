#Input

import heapq

tc = int(input())
while tc > 0:
    N, k = [int(i) for i in input().split()]
    A_N = [int(i) for i in input().split()]
    A_K = sorted(heapq.nlargest(k, A_N), reverse=True)

    print(*A_K)
    tc -= 1
