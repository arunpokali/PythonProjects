#BBABCBCAB

str1 = input()
str2 = "".join(reversed(str1))


long_sub = [[0 for x in range(len(str2) + 1)] for i in range(len(str1) + 1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        #print(str1[i], str2[j])

        if str1[i] == str2[j]:
            long_sub[i+1][j+1] = long_sub[i][j] + 1
        else:
            long_sub[i+1][j+1] = max(long_sub[i][j+1], long_sub[i+1][j])

for i in long_sub:
    print(i)

i = len(str1)
j = len(str2)

lcs = []

for _ in range(max(i, j)):
    print(i, j, long_sub[i][j], long_sub[i-1][j], long_sub[i][j-1])
    if i > 0 and j > 0:
        if long_sub[i][j] == long_sub[i-1][j]:
            i -= 1
        if long_sub[i][j] == long_sub[i][j-1]:
            j -= 1
        if long_sub[i][j] > long_sub[i-1][j] and long_sub[i][j] > long_sub[i][j-1]:
            print(str1[i-1])
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
    else:
        break
    print(lcs)

print(lcs)
