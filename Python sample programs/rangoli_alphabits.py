import string

#print(string.ascii_lowercase[0])

n = int(input())

assert n in range(1, 27)


for x in reversed(range(n)):
    print(x)
    for y in reversed(string.ascii_lowercase[:x+1]):
        print(y)



450000
460000
470000
480000
500000
510000
520000
530000
540000
12510
12780
12960
13140
13230
13320
13620
13920
14160
14400
14580

