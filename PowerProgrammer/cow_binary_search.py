def Cows_largest_min_dist(Stall_p, cow_c ):
    print(Stall_p)
    high = Stall_p[len(Stall_p)-1] - Stall_p[0]
    low = 1
    print(high,low)
    intial = Stall_p[0]
    while low < high:
        print(high,low)
        cow_count=1
        mid = low + (high-low + 1)//2
        print(high,low,mid)
        intial = Stall_p[0]
        print(Stall_p)
        for i in range(1,len(Stall_p)):
            print("Stall_p[i] >= mid + intial :" , Stall_p[i]," ,", mid ,",", intial  )
            if Stall_p[i] >= mid + intial :
                cow_count += 1
                intial = Stall_p[i]

        print("mid: ", mid, ", cow_coutn " ,cow_count)

        if cow_count < cow_c:
            high = mid -1
        else:
            low = mid

    return low


def main():
    TC = int(input())
    while TC > 0:

        N_stall, N_cows = [int(x) for x in input().split()]

        Stall_pos = []

        for i in range(N_stall):
            Stall_pos.append(int(input()))

        print(Cows_largest_min_dist(sorted(Stall_pos),N_cows))
        TC -= 1

if __name__ == '__main__':
    main()
