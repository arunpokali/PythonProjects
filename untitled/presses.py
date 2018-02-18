def presses(phrase):
    alpha_num={1:{'a','d','g','j','m','p','t','w',' ','1'},2:{'0','b','e','h','k','n','q','u','x'},3:{'c','f','i','l','o','r','v','y'},4:{'s','z','2','3','4','5','6','8'},5:{'7','9'}}
    press_count=0
    for char in phrase.lower() :
        for k in alpha_num :
            if char in alpha_num[k] :
                press_count=press_count+k
    return press_count

#your code here