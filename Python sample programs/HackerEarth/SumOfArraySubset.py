arr_len = int(input())
arr = [int(x) for x in input().split()]
sum_subarr = int(input())

def binarySearch():
    print()


def subset_arr(arr_v, x):
    for i in range(len(arr_v) - 1):
        sum_v = 0
        for j in range(i,len(arr_v)-1):
            sum_v += arr_v[j]
            c = x - sum_v

            if c > arr_v[j]:
                pos = binarySearch(c, j, len(arr_v)-1)



            else:
                break


