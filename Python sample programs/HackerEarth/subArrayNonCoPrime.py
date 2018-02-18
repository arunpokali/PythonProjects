

def GCD(p, q):
    if p >= q:
        while p % q != 0:
           p, q = q, p % q

        return q
    else:
        while q % p != 0:
            q, p = p, q % p

        return p


def isSubArrayNonCoPrime(arr, s, e):

    global count
    global dp


    if e-s == 1 and dp[s][e] is None:
        #print("GCD of ", arr[s],",",arr[e]," is ", GCD(arr[s], arr[e]))

        if GCD(arr[s], arr[e]) != 1:
            count += 1
            dp[s][e] = True
            return True
        else:
            dp[s][e] = False
            return False

    elif dp[s][e] is not None:
        #print("ELIF :")
        return dp[s][e]

    else:
        #print("ELSE")
        x = isSubArrayNonCoPrime(arr, s, e-1)
        y = isSubArrayNonCoPrime(arr, s+1, e)
        if x and y:
            count += 1
            dp[s][e] = True
            return True
        else:
            dp[s][e] = False
            return False

arr_len = int(input())

arr_r = [int(x) for x in input().split()]

count = 0

dp = [[None] * arr_len for _ in range(arr_len)]

isSubArrayNonCoPrime(arr_r, 0, arr_len-1)

# print(dp)
for x in dp:
    print(x)
print(count+arr_len)


