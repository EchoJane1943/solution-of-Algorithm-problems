'''
冒泡排序算法的原理如下：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后k个(第k+1次)。一共循环n-1次。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较

Worst case performance	O(n2)
Best case performance	O(n)
Average case performance	O(n2)
'''

# 冒泡排序是稳定的。算法时间复杂度是O(n^2)。
def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
    
l = [45, 32, 8, 33, 12, 22, 19, 97]
bubble_sort(l)
