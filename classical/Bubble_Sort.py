'''
冒泡排序算法的原理如下：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了第一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
'''

# 冒泡排序是稳定的。算法时间复杂度是O(n^2)。
l = [45, 32, 8, 33, 12, 22, 19, 97]
def bubble_sort(l):
    n = len(l)
    j = 1
    while j < n:
        for i in range(n-j-1):
            if l[i]>l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
        j+=1
    return l
bubble_sort(l)
