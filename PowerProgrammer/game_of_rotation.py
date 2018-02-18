#n = int(input())

n_arr = [int(x) for x in input().strip().split()]
n = len(n_arr)

def brute_force(n_arr,n):
    pmean = 0

    for k in range(n):
        n_arr = n_arr[-1:] + n_arr[:-1]
        mean = 0
        for i, v in enumerate(n_arr):
            mean += (i+1) * v
        if k == 0 :
            pmean = mean
        else:
            pmean = max(mean,pmean)
        #print(mean,pmean)
    print(pmean)

def optimum(n_arr, n):
    sum_t = sum(n_arr)
    T = 0
    for i,v in enumerate(n_arr):
        T += (i+1) * v
    pmean = T
    for i in reversed(range(1,n)):
        mean = T + sum_t - (n * n_arr[i])

        pmean = max(pmean, mean)
        T = mean
    print(pmean)

optimum(n_arr,n)