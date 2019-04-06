'''
简单选择排序是最简单直观的一种算法，
基本思想为每一趟从待排序的数据元素中选择最小（或最大）的一个元素作为首元素，直到所有元素排完为止，
简单选择排序是不稳定排序
'''

def selection_sort(l):
    n = len(l)
    if n<=1:
      return l
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if l[j] < l[mini]:
                mini = j
        l[i],l[mini] = l[mini],l[i]
    return l
           
l = [45, 32, 8, 33, 12, 22, 19, 97]
selection_sort(l) 
