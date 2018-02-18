#Write a function that takes a single string (word) as argument.
#  The function must return an ordered list containing the indexes of all capital letters in the string.

def capitals(word):
    upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word_list=[]
    i=0
    print(len(word))
    while i<len(word) :
        if word[i] in upperLetters :
            word_list.append(i)
        i+=1
    return word_list

print(capitals("dsIHH3kkI"))
import timeit
print(timeit.timeit("capitals('aRn')", setup="from __main__ import capitals"))