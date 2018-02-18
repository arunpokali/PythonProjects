str1 = input()
str2 = input()


long_sub = [[0 for x in range(len(str2) + 1)] for i in range(len(str1) + 1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        #print(str1[i], str2[j])

        if str1[i] == str2[j]:
            long_sub[i+1][j+1] = long_sub[i][j] + 1
        else:
            long_sub[i+1][j+1] = max(long_sub[i][j+1], long_sub[i+1][j])

print(long_sub[-1][-1])

