TC = int(input().strip())


it = 1

def maxSubArraySum(a,size):

    max_so_far = 0
    max_ending_here = 0
    Nc_max = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if (a[i] > 0):
            Nc_max += a[i]

    return (max_so_far,Nc_max)

while it <= TC :
    high = int(input().strip())
    in_list = [int(i) for i in input().strip().split()]

    a , b = maxSubArraySum(in_list,high)
    if a > 0 :
        print(a,b)
    else :
        print(-1,b)
    it += 1