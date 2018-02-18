def xo(s):
    count_x,count_o=0,0
    for i in s :
        if i=='x' or i=="X" :
            count_x += 1
        elif i=='o' or i=='O' :
            count_o +=1
    print(count_x,count_o)
    if count_x == count_o :
        return True
    else :
        return False

print(xo('hsxxOOlfxos)'))
print(xo('xpdLkxxxOxQhCrxxOOfJxEOUOxOOxOOOOxSxxOOxxOOOxOAGxNxOObmtx'))

def xo(s):
    count_o=s.count('o')+ s.count("O")
    count_x=s.count('x')+s.count('X')

    if count_x == count_o :
        return "x0_2"
    else :
        return False


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('xxxxxxxxxxxxxxoxoooxoxxooxxooxbooxxoxAooxox'))
#print(xo('hsxxOOlfxos)','g'))