import sys

sys.setrecursionlimit(2000)

def rec(strg,l_pwd, res_str):
    print(res_str,strg)
    for i in range(len(strg)):
        if strg[:i+1] in l_pwd:
            if i+1 != len(strg):
                res_str.append(strg[:i+1])
                val = rec(strg[i+1:],l_pwd, res_str)
                if not val :
                    res_str.pop(-1)
                    #print(res_str)
                else:
                    return True
                
            else:
                res_str.append(strg[:i+1])
                #print(res_str,"True")
                return True
     
    else:
        #print(res_str,"False")
        return False
                #add the strg[:i+1] to res_str
                
                
def solve():
    n = int(input())
    l_pwd = [ x for x in input().split()]
    con_pwd = input()
    res_str = []
    rec(con_pwd,l_pwd,res_str )
    if len(res_str) == 0 :
        print("Wrong Password", end='')
    else:
        for i in res_str:
            print(i, end=" ")
    
           


for _ in range(int(input())):
    solve()
    print()