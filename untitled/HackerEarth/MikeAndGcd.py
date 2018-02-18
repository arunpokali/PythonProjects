list_len = int(input())
list_ele = [int(i) for i in input().strip().split()]
list_out = []
gdc_dp = [[0] * list_len for i in range(list_len)]

def gcd(a, b):


    p, q = list_ele[a] , list_ele[b]
    # noinspection PyTypeChecker
    if gdc_dp[a][b] is 0 and gdc_dp[b][a] is 0:

        if p >= q:
            while p%q != 0 :
               p, q = q, p%q

            gdc_dp[a][b] = q

            return q
        else :
            while q%p != 0 :
               q, p = p, q%p

            gdc_dp[a][b] = p

            return p
    else :

        return max(gdc_dp[a][b], gdc_dp[b][a])

for i in range(list_len):
    # index_l = -1
    #print(i,list_ele[i])
    index = -1
    for j in range(1, max(list_len - i, i)+1):
        #print(max(list_len - i, i),'max')
        #print('i', i,'j',j)

        gcd_l, gdc_r = 0, 0
        if i - j >= 0:
            gcd_l = gcd(i, i-j)
            #print(gcd_l,list_ele[i],list_ele[i-j])
        if i + j < list_len:
            gcd_r = gcd(i, i+j)
            #print(gcd_r,list_ele[i],list_ele[i+j])

        if gcd_l > 1:
            index = i - j +1
            break
        if gcd_r > 1:
            index = i + j +1
            break
    #print('index',index)
    list_out.append(index)

#print(' '.join(map(str, list_out)))
print(*list_out)

