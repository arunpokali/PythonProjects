
# Unbound Knapsack Example Both Min & Max using Rod Cut Problem

# 0 is default value since we want max value , For min
# give some large value and DP[0] is 0 for both max & min


def Max_Rod_Value_Values(Rod_Length, Rod_Price_List):

    DP = [[0, []] for _ in range(Rod_Length+1)]

    for i in range(1, Rod_Length + 1):
        for j in range(len(Rod_Price_List)):
            if i >= (j+1):
                # DP[i] = max(DP[i], DP[i-(j+1)]+Rod_Price_List[j])
                if DP[i][0] < DP[i-(j+1)][0] + Rod_Price_List[j]:
                    DP[i][0] = DP[i-(j+1)][0] + Rod_Price_List[j]
                    DP[i][1] = DP[i][1] + DP[i-(j+1)][1] + [j+1]

    print(DP)
    return( (DP[-1][0], set(DP[-1][1])) )


def Max_Rod_Value(Rod_Length, Rod_Price_List):

    DP = [0 for _ in range(Rod_Length+1)]

    for i in range(1, Rod_Length + 1):
        for j in range(len(Rod_Price_List)):
            if i >= (j+1):
                DP[i] = max(DP[i], DP[i-(j+1)]+Rod_Price_List[j])

    return DP[-1]


def Min_Rod_Value(Rod_Length, Rod_Price_List):

    DP = [10**7 + 9 for _ in range(Rod_Length+1)]
    DP[0] = 0
    for i in range(1, Rod_Length + 1):
        for j in range(len(Rod_Price_List)):
            if i >= (j+1):
                DP[i] = min(DP[i], DP[i-(j+1)]+Rod_Price_List[j])

    return DP[-1]


def Min_Rod_Value_Values(Rod_Length, Rod_Price_List):

    DP = [[10**7 + 9, []] for _ in range(Rod_Length+1)]
    DP[0][0] = 0
    for i in range(1, Rod_Length + 1):
        for j in range(len(Rod_Price_List)):
            if i >= (j+1):
                #DP[i] = min(DP[i], DP[i-(j+1)]+Rod_Price_List[j])
                if DP[i][0] > DP[i-(j+1)][0] + Rod_Price_List[j]:
                    DP[i][0] = DP[i-(j+1)][0] + Rod_Price_List[j]
                    DP[i][1].append(j+1)

    print(DP)
    return DP[-1]


Rod_Length = int(input())

Rod_Price_List = [int(x) for x in input().split()]

print("Max value is : ", Max_Rod_Value_Values(Rod_Length, Rod_Price_List))

# print("Min value is : ", Min_Rod_Value_Values(Rod_Length, Rod_Price_List))

