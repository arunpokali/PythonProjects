def merge_sort(u_list,first,last):

    if first < last:

        mid = (first+last)//2

        u_list = merge_sort(u_list, first, mid)
        u_list = merge_sort(u_list, mid+1, last)

        u_list = merge(u_list, first, mid, last)

    return u_list

def merge(ulist, f, m, l):

    nlist, mm, ff = [], m+1, f
    print('ulist', ulist, 'f m l', f, m, l)
    while f <= m and mm <= l:

        if ulist[f] < ulist[mm]:
            nlist.append(ulist[f])
            print('nlist inside >', nlist)
            f += 1
        else:
            nlist.append(ulist[mm])
            mm += 1
    print('nlist', nlist, 'ulist[f:m]', ulist[f:m+1], 'ulist[mm:l]', ulist[mm:l+1])

    if f > m:
        nlist[len(nlist)+1:] = ulist[mm:l+1]

    if mm > l:
        nlist[len(nlist)+1:] = ulist[f:m+1]

    print('nlist', nlist, 'ulist[:f]', ulist[:f], "ulist[l+1:]", ulist[l+1:] )

    ulist = ulist[:ff] + nlist + ulist[l+1:]

    print('ulist after merge', ulist)
    return ulist

print(merge_sort([5, 3, 6, 7, 2], 0, 4))







