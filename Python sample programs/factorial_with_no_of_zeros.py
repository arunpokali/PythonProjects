def factorize_5(num):
    count, i = 0, 1

    while num > pow(5, i):
        count += num//pow(5, i)
        print(count)
        i += 1

    return count

print("The no. of 5 factors in then numbers factorial", factorize_5(260))