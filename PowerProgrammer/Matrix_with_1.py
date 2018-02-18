"""
Solution
1) Declare dp = [][]
Dp matrix contains the value of largest square with all 1's having Dp[i][j]
as right-bottom most square.
"""

m, n = [int(x) for x in input().split()]

matrix = []

for _ in range(m):
    matrix.append([int(x) for x in input().split()])

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]


for i in range(1,m+1):
    for j in range(1)