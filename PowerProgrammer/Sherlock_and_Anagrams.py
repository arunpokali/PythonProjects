from collections import *
for i in range(int(input())):
    s = input()
    check = defaultdict(int)
    l = len(s)
    for i in range(l):
        for j in range(i+1, l+1):
            sub = list(s[i:j])
            print(sub)
            sub.sort()
            sub = "".join(sub)
            check[sub] += 1

    print(check)
    check['a'] = 3
    sum = 0
    for i in check:
        print(i, check[i])
        n = check[i]
        sum += (n*(n-1))/2
    print(sum)
