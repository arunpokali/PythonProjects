def breakChocolate(m,n) :
    if isinstance(m,int) and isinstance(n,int) and m >0 and n >0 :
        return (m*n -1)
    else:
        return 0

print(breakChocolate(3,7))