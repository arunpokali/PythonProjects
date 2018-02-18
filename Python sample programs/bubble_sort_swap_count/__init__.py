# print("Hello World!")
list_len = int(input())
list_ele = [int(i) for i in input().strip().split()]

#print(list_len)
swap_count = 0

for p in range(list_len):

    for q in range(list_len - p -1):
        if list_ele[q] > list_ele[q + 1]:
            list_ele[q], list_ele[q + 1] = list_ele[q + 1], list_ele[q]
            swap_count += 1

print(swap_count)
