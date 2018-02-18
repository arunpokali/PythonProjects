import sys

def getWays(n, c):
    # Complete this function
    S = c
    m = len(c)
    
    table = [0 for k in range(n+1)]

    table[0] = 1

    for i in range(0,m):
        # print(S[i], n+1)
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
            # print(j, table[j])
        # print("\n")
    print(table)
    return table[n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
