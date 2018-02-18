def solve(arr, n):
    dp = [ [0,0,0] for x in range(n) ]
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][1], dp[i-1][0])


    return min(dp[-1])


for _ in range(int(input())):

    n = int(input())
    arr = []
    for _ in range(n):
        tem = [ int(x) for x in input().split()]
        arr.append(tem)
    ans = solve(arr,n)
    print(ans)