# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):

    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n+1)]

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0,m):
        # print(S[i], n+1)
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
            # print(j, table[j])
        # print("\n")
    # print(table)
    return table[n]

# Driver program to test above function
arr = [int(x) for x in input().split()]
m = len(arr)
n = int(input())
x = count(arr, m, n)
print(x)
