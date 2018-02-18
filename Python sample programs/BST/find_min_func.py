N = int(input())

N_list = []

for i in range(N):
    N_list.append([int(i) for i in (input().strip().split())])

for each_list in N_list:
    #print(each_list)
    if each_list[0] < 3 and each_list[1] < 3:
        print(2 * each_list[1] ** 2 - 12 * each_list[1] + 7)
    elif each_list[0] <= 3 <= each_list[1]:
        print("-11")
    else:
        print(2 * each_list[0] ** 2 - 12 * each_list[0] + 7)
