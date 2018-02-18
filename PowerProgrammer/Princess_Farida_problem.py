tc = int(input())
case = 1

while tc > 0:
    N = int(input())
    if N == 0:
        print("Case", case, ": ", 0)
        case += 1

    elif N == 1:
        Arr = [int(x) for x in input().split()]
        print("Case", case, ": ", Arr[0])
        case += 1
    else:
        Arr = [int(x) for x in input().split()]
        DP = [0] * N

        DP[0] = Arr[0]
        DP[1] = max(Arr[0], Arr[1])

        for i in range(2, N):
            DP[i] = max(DP[i - 1], DP[i - 2] + Arr[i])

        print("Case", case, ": ", DP[i])
        case += 1

    tc -= 1
