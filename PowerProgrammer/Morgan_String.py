
tc = int(input())

for _ in range(tc):
    str1 = list(input())
    str2 = list(input())
    # mx = max(len(str1), len(str2))
    # mn = min(len(str1), len(str2))
    s = ""
    for i in range(len(str1) + len(str2)):

        if len(str1) > 0 and len(str2) > 0:
            if str1[0] > str2[0]:
                s += str2.pop(0)
            elif str1[0] < str2[0]:
                s += str1.pop(0)
            else:

        elif len(str1) == 0:
            s += "".join(str2)
            break
        elif len(str2) == 0:
            s += "".join(str1)
            break
        #print(s, ",", str1, " , ", str2)
    print(s)





