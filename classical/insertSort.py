def insertSort(l):
    n = len(l)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if l[i] < l[j]:
                l[i],l[j]=l[j],l[i]
                i = j
    return l
l = [45, 32, 8, 33, 12, 22, 19, 97]
insertSort(l)
