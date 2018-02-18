from collections import defaultdict

n, k = [int(x) for x in input().strip().split()]
n_l = [int(x) for x in input().split()]
# n_r = [x % k for x in n_l]

def sol_2(r_k, r_n_l):
    subset_dict = defaultdict(lambda: [0, []])
    for val in r_n_l:
        subset_dict[val % r_k][1].append(val)
        subset_dict[val % r_k][0] += 1
    
    count = 0

    if subset_dict[0][0] > 0:
        count += 1

    if r_k % 2 == 0:
        subset_dict[r_k/2][0] = min(subset_dict[r_k/2][0], 1)

    for i in range(1, (r_k//2) + 1):
        count += max(subset_dict[i][0], subset_dict[r_k-i][0])
       
    print(count)
    
if __name__ == '__main__':
    sol_2(k, n_l)