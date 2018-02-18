from collections import defaultdict
def solve():
    n = int(input())
    in_cor = []
    d_set = defaultdict(set)
    for _ in range(n):
        a, b = input().split()
        a, b = int(a), int(b)
        in_cor.append((a,b))

    for i in range(n):
        p, q = in_cor[i]
        #print(p,q)
        for j in range(i+1,n):
            x, y = in_cor[j]
            if x-p != 0 and y-q != 0:
                sl = ((x-p)/(y-q))
                if sl == 1 :
                    k_x = x - y
                    # d_set[(k_x,0)]= set()
                    print(p,q,",", x,y)
                    d_set[(k_x,0)].add((x,y))
                    d_set[(k_x,0)].add((p,q))
                    print(d_set)

                if sl == -1 :
                    k_y = y - x
                    # d_set[(0,k_y)]= set()
                    d_set[(0,k_y)].add((p,q))
                    d_set[(0,k_y)].add((x,y))


    print(d_set)
    count = 0
    for val in d_set.values():
        l = len(val)
        count += (l * (l - 1)) // 2

    return count
tc = int(input())
while(tc):
    res = solve()
    print(res)
    tc = tc - 1