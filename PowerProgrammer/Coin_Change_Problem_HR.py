

def coin_change(change_for, change_list):

    DP = [0 for _ in range(change_for+1)]

    for i in range(1, change_for + 1):
        for j in change_list:
            print("i,J :", i, ",", j)
            if i >= j:

                if i-j == j and i % j == 0:
                    DP[i] += DP[i-j]

                elif i % j == 0:
                    DP[i] += 1

                bl = i-j not in change_list
                if i-j < j or bl:
                    DP[i] += DP[i-j]

            print("DP:", DP)
        print("\n")
        print(DP)
    return DP[-1]

c_f = int(input())
c_l = [int(x) for x in input().split()]
print(coin_change(c_f, c_l))


