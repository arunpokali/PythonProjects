INF = 10 ** 18


def one_test():
    n = int(input())
    a = list(reversed(list(map(int, input().split()))))
    print('a : ', a)
    dp = [0] * (n + 1)
    for i in range(n):
        take = 0
        dp[i + 1] = -INF
        for j in range(i, max(i - 3, -1), -1):
            print("i, j :", i, ",", j, ",", a[j])
            take += a[j]
            print("take, dp[j], dp[i +1]: ", take, ",", dp[j], ",", dp[i + 1])
            dp[i + 1] = max(dp[i + 1], take - dp[j])
            print("dp[", i + 1, "]: ", dp[i + 1])
    print("!!!", dp)
    return (sum(a) + dp[n]) // 2


def dp_brick_game():
    n = int(input())
    arr = list(reversed(list(map(int, input().split()))))
    # print(arr)
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = arr[0] + arr[1] + arr[2]

    sum = [0 for _ in range(n)]
    sum[0] = arr[0]

    for i in range(1, n):
        sum[i] = sum[i - 1] + arr[i]

    # print('sum: ', sum)

    for i in range(3, n):

        dp[i] = max(arr[i] + (sum[i-1] - dp[i - 1]), arr[i] + arr[i - 1] + (sum[i-2] - dp[i - 2]),
                    arr[i] + arr[i - 1] + arr[i - 2] + (sum[i-3] - dp[i - 3]))
        # print(dp)
    # print(dp)
    return dp[-1]
t = int(input())
for i in range(t):
    print(dp_brick_game())


