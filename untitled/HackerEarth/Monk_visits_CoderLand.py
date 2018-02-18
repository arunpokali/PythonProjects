TestCases = int(input())

for k in  range(TestCases) :
    N = int(input())
    Cost_petrol = [int(x) for x in input().split()]
    Dist_next_checkpoint = [int(x) for x in input().split()]

    min_cost_petrol = Cost_petrol[0]

    Cost = 0

    for i in range(N):
        if min_cost_petrol > Cost_petrol[i]:
            min_cost_petrol = Cost_petrol[i]
            Cost += (min_cost_petrol * Dist_next_checkpoint[i])
        else :
            Cost += (min_cost_petrol * Dist_next_checkpoint[i])


    print(Cost)
