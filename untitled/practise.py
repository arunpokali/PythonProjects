def modify(arr, t, i, j):
    if t == 1:
        return arr[i:j+1] + arr[:i] + arr[j+1:]

    if t == 2:
        return arr[:i] + arr[j+1:] + arr[i:j+1]


N, M = [int(x) for x in input().split(' ')]
arr = [int(x) for x in input().split(' ')]

#print(arr, type(arr[0]))

que = [None]
for i in range(M):
    que = [int(x) for x in input().split(' ')]
    arr = modify(arr, que[0], que[1]-1, que[2]-1)


    #print(arr)
print(abs(arr[0]-arr[N-1]))
print(' '.join([str(x) for x in arr]))
