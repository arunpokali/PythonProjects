def sherlock_1():
    n = int(input())
    b = list(map(int, input().split(' ')))

    l, h = 0, 0
    for i in range(1, n):
        l, h = (max(l, h + b[i - 1] - 1), max(l + b[i] - 1, h + abs(b[i] - b[i - 1])))
        print(l, h)
    print(max(l, h))


def sherlock_dp():
    n = int(input())
    b = list(map(int, input().split(' ')))
    dp = [[0, 0] for _ in range(n)]
    dp[1][0] = 1
    dp[1][1] = b[0]

    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + b[i-1] - 1)
        dp[i][1] = max(dp[i-1][1] + b[i] - 1, dp[i-1][1] + abs(b[i] - b[i-1]))
        # print(dp[i])
    print(max(dp[n-1]))

for _ in range(int(input())):
    sherlock_dp()

