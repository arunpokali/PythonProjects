n=int(input())

#taking value range upto iterate and find reversible numbers
_input_var = [int(input()) for i in range(0,n)]


#function will reverse the number and return
def reverse(num):
	return int(str(num)[::-1])

#function will check odd confirmation for every digit
def isDigitOdd(num):
	lista = str(num)
	for i in lista:
		if int(i)%2==0:
			flag = False
			return flag
		else:
			flag = True
	return flag

#main method
def main(_iter):
    count=0
    for i in range(0, _iter):
        k = i + reverse(i)
        if i % 10 != 0 and isDigitOdd(k):
            count += 1

    print(count)

#calling main method for N number ranges
for i in _input_var:
	main(i)