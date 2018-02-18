def qsort(ulist, f, l):
    if f < l :
        par = partition(ulist, f, l)

        qsort(ulist, , par -1)
        qsort(ulist, par + 1, l)

    return  ulist

def partition():





def quicksort(ulist):

    print("List before sorting", ulist)
    ulist = qSort(ulist, 0, len(ulist))
    print("List after sorting", ulist)

quickSort([4,2,5,12,8,1])