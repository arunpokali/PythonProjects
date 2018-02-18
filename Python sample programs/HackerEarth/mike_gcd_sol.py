import math
import bisect


N = int(input())
A = [int(x) for x in input().split()]

factorsmap = dict()

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    print('In index func :')
    i = bisect.bisect_left(a, x)
    print(" i ", i, 'len(a)', len(a), "a[i]", a[i], "a ", a, "x", x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def factors(x):
    if x == 1:
        return set()
    print('factorsmap :',factorsmap, ', x :', x)
    if x in factorsmap:
        return factorsmap[x]

    print('int(math.sqrt(x))+1  :', int(math.sqrt(x)) + 1)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            temp = set()
            temp.add(i)
            print('added i to temp :', i, temp)
            print('calling factors with :', x/i)
            temp = temp.union(factors(x / i))
            factorsmap[x] = temp.copy()
            print('temp in if , x ,  factorsmap:', temp, x,  factorsmap)
            return temp
    temp = set()
    temp.add(x)
    factorsmap[x] = temp.copy()
    print('temp  , x ,  factorsmap:', temp, x,  factorsmap)
    return temp

factor_to_index = dict()


for i, x in enumerate(A):
    for factor in factors(x):
        print('x, factor :', x, factor)
        if factor not in factor_to_index:
            factor_to_index[factor] = []
        factor_to_index[factor].append(i)
        print('factor_to_index , x :', factor_to_index, x)

for key in factor_to_index:
    factor_to_index[key].sort()

print('factor to index after sort :', factor_to_index)
print('factorsmap : ', factorsmap)
result = []
for i, x in enumerate(A):
    fs = factors(x)
    print('i, x ,fs :', i, x, fs)
    closest = -2 * len(A)
    print('closest :', closest)
    for factor in fs:
        print('calling index :', factor_to_index[factor],factor, i)
        loc = index(factor_to_index[factor], i)
        print('loc :', loc)
        if loc > 0:
            item = factor_to_index[factor][loc-1]
            print('item :', item)
            if abs(item - i) <= abs(closest - i):
                closest = item
        if loc < len(factor_to_index[factor])-1:
            item = factor_to_index[factor][loc+1]
            print('item ::', item)
            if abs(item - i) < abs(closest - i):

                closest = item

    print('closest ::', closest)
    if closest >= 0:
        result.append(closest+1)
    else:
        result.append(-1)

print(" ".join([str(x) for x in result]))
