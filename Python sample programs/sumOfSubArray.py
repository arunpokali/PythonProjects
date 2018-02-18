TC = int(input().strip())


it = 1

while it <= TC :
    high = int(input().strip())
    in_list = [int(i) for i in input().strip().split()]
    sum_sub = []
    t_sum = 0
    #high = len(in_list)
    dp = [[None for i in range(high)] for i in range(high)]
    #print(in_list)
    def sum_con(li, low, high):

        if dp[low][high] is not None :
            #print('Found In dp', low, high, dp[low][high])
            return dp[low][high]

        if high - 1 > low :
            t_sum = sum_con(li, low+1, high)
            dp[low][high] = li[low] + t_sum
            #print('processing [low][high]', low, high, dp[low][high])

            #print(dp)
            """for j in range(len(li)):
                print(dp) """

            return dp[low][high]

        else :
            t_sum = li[low] + li[high]
            dp[low][high] = t_sum
            #print('leaf processing [low][high]', low, high, dp[low][high])
            #print(dp)
            return t_sum

    for i in range(high):
        for j in range(i+1, high):
            sum_sub.append(sum_con(in_list, i, j))

    #nc_sum =0

    #sum([j for j in in_list if j > 0 ])
    print(max(sum_sub), sum([j for j in in_list if j > 0 ]))
    it += 1
