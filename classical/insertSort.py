'''
插入即表示将一个新的数据插入到一个有序数组中，并继续保持有序。
例如有一个长度为N的无序数组，进行N-1次的插入即能完成排序；
第一次，数组第1个数认为是有序的数组，将数组第二个元素插入仅有1个有序的数组中；
第二次，数组前两个元素组成有序的数组，将数组第三个元素插入由两个元素构成的有序数组中......
第N-1次，数组前N-1个元素组成有序的数组，将数组的第N个元素插入由N-1个元素构成的有序数组中，则完成了整个插入排序。

思想：
进行n-1次排序，第i次排序，将第i+1个数分别与前i个数据比较，找到合适的位置。
找法为：l[i+1]与l[i]比较，排序，跟踪l[i+1]的位置。
'''

def insertSort(l):
    n = len(l)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if l[i] > l[j]:
                break
            elif l[i] < l[j]:
                l[i],l[j]=l[j],l[i]
                i = j
    return l
l = [45, 32, 8, 33, 12, 22, 19, 97]
insertSort(l)
