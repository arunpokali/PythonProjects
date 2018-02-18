val = [int(x) for x in input().split()]
weight = [int(x) for x in input().split()]

K_W = int(input())

#DP = [ for k in range(len(val)+1)]
DP = [[0 for x in range(K_W+1)] for x in range(len(val))]


for k in range(1, K_W+1):
    print(weight[0], k)
    if weight[0] <= k:

        DP[0][k] = val[0]

print(len(DP), len(DP[1]), DP[0])

for i in range(1, len(val)):
    for j in range(1, K_W+1):
        #print("i", i)
        if weight[i] > j:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(val[i] + DP[i-1][j-weight[i]], DP[i-1][j])


print("max value of KS", DP[-1][-1])
print(DP)
