
def solve_X(arr,n,X,Y):
    amount = 0
    for i in range(n-2,0,-1):
        #print(i,arr[i])
        amount += X * (arr[i] - arr[0]) +  Y * (arr[i+1] - arr[i])
        print(amount)

    return amount

def solve_Y(arr,n,X,Y):

    amount = 0
    for i in range(1,n-1):
        amount += Y * (arr[i] - arr[i-1]) + X * (arr[-1] - arr[i])
        print(amount)
    return amount

def solve(arr,n,X,Y):

    #print("In solve",n)

    if n <= 2 :
        #print("less than 2",n)
        return 0

    mid = n//2
    #print(mid,arr)
    amount = X*(arr[mid]-arr[0]) + Y*(arr[-1]-arr[mid]) + solve(arr[0:mid+1],len(arr[0:mid+1]),X,Y) + solve(arr[mid:],len(arr[mid:]),X,Y)
    #print(amount,mid)
    return amount

for _ in range(int(input())):

    X,Y = [ int(x) for x in input().split()]
    n = int(input())
    arr = [ int(x) for x in input().split()]

    print(solve_X(arr,n,X,Y), solve_Y(arr,n,X,Y), solve(arr,n,X,Y) )
