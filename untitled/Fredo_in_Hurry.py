N_TC = int(input())

L_Floor = []

for i in range(N_TC):
    L_Floor.append(int(input()))

print('floor list', max(L_Floor)//2)

L_By_Foot = []

for floor in range(max(L_Floor)//2):
    L_By_Foot.append(floor + (floor * (floor + 1))//2)

print(L_By_Foot)

for Given_floor in L_Floor:
    for i, min_val in enumerate(L_By_Foot):
        if Given_floor >= min_val :
            By_foot_floor = i
        else:
            break
    if Given_floor == 1 :
        print(1)
    else:
        print((Given_floor - By_foot_floor)*2)
