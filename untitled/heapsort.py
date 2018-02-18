# HeapSort : I am trying to implement HeapSort, So how implement?
# Take a list of unsorted numbers as input
#
def heapify(a, l, le):
    # c=(l/2)-1

    for i in reversed(range(l)):

        if le - 1 > 2 * i + 1:

            if a[i] < a[2 * i + 1] or a[i] < a[2 * i + 2]:

                if a[2 * i + 1] > a[2 * i + 2]:
                    temp = a[i]
                    a[i], a[2 * i + 1] = a[2 * i + 1], temp
                elif a[2 * i + 1] < a[2 * i + 2]:
                    temp = a[i]
                    a[i], a[2 * i + 2] = a[2 * i + 2], temp


        else:

            if a[i] < a[2 * i + 1]:
                temp = a[i]
                a[i], a[2 * i + 1] = a[2 * i + 1], temp


def heapsort(ar):
    for i in reversed(range(len(ar))):
        heapify(ar, (i + 1) // 2, i + 1)

        t = ar[0]
        ar[0], ar[i] = ar[i], t

    print(ar)


heapsort([5444, 302, 46, 77, 4300, 540, 2, -89, 0, 9])
