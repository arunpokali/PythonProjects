n_l = [ int(x) for x in input().split()]

dp = [[0, 0] for x in range(len(n_l))]

if n_l[0] % 2 == 0:

    dp[0][1] = n_l[0]
else:
    dp[0][0] = n_l[0]

print(dp[0])
for i, val in enumerate(n_l[1:]):
    j = i+1
    print(val)
    if val%2 == 0 :
        dp[j][1]= dp[j-1][1] + val
        dp[j][0]= dp[j-1][0]
    else:
        print(dp[j-1][0] + val, dp[j-1][1] + val)
        dp[j][0] = max(dp[j-1][0] + val, dp[j-1][1] + val)
        dp[j][1] = dp[j-1][1]

    print(dp[j])

print(max(dp[-1][0], dp[-1][1]))

