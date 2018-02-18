
def solve_1(ar,l,num,ss):
    max_v = 0
    k =l-num
    for m in range(k+1):
            print(ar[-1 -k + m], ar[m] ,l-k, (l-k) * ( ar[-1 -k + m] - ar[m] ))
            if ss >= (l-k) * (ar[-1 -k + m] - ar[m]) > max_v:
                max_v = (l-k) * ( ar[-1 -k + m] - ar[m])


    return max_v

def solve(ar, l, ss):

    if l * (ar[-1]-ar[0]) <= ss:
        return l

    for k in range(l):
        print(k)
        for m in range(k+1):
            print(ar[-1 -k + m], ar[m] ,l-k, (l-k) * ( ar[-1 -k + m] - ar[m] ))
            if (l-k) * ( ar[-1 -k + m] - ar[m] ) <= ss :
                return l-k


for _ in range(int(input())):
    n, s = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    K = solve(arr,n, s)
    print()
    V = solve_1(arr,n, K, s)
    print(K,V)

#
# 1
# 7 40
# 2 4 7 9 14 15 22