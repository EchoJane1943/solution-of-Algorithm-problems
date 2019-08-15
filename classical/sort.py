# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
l = [1,3,2,6,9,33,66,44]
# 蒂姆排序
# -*- coding:utf-8 -*-
def tim_sort(lst):
    if not lst:
        return []
    lst.sort()
    return lst

tim_sort(l)

# 快速排序
# -*- coding:utf-8 -*- 
def quick_sort(lst):
    if not lst:
        return []
    pivot = lst[0]
    left = quick_sort([x for x in lst[1:] if x < pivot])
    right = quick_sort([x for x in lst[1:] if x >= pivot])
    return left + [pivot] + right

quick_sort(l)

# 归并排序
# -*- coding:utf-8 -*-
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left,right)
def merge(left,right):
    l,r,res = 0,0,[]
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]
    return res
merge_sort(l)

# 堆排序
def siftup(lst, temp, begin, end):
    if lst == []:
        return []
    i, j = begin, begin * 2 + 1
    while j < end:
        if j + 1 < end and lst[j + 1] > lst[j]:
            j += 1
        elif temp > lst[j]:
            break
        else:
            lst[i] = lst[j]
            i, j = j, 2 * j + 1
    lst[i] = temp
 
def heap_sort(lst):
    if lst == []:
        return []
    end = len(lst)
    for i in range((end // 2) - 1, -1, -1):
        siftup(lst, lst[i], i, end)
    for i in range(end - 1, 0, -1):
        temp = lst[i]
        lst[i] = lst[0]
        siftup(lst, temp, 0, i)
    return lst
heap_sort(l)

# 冒泡排序
# -*- coding:utf-8 -*-
def bubble_sort(lst):
    if not lst:
        return []
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst
bubble_sort(l)

# 直接选择排序
# -*- coding:utf-8 -*-
def select_sort(lst):
    if lst == []:
        return []
    for i in range(len(lst)-1):
        smallest = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
 
    return lst
select_sort(l)

# 插入排序
def Insert_sort(lst):
    if lst == []:
        return []
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i
        while j > 0 and temp < lst[j - 1]:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = temp
    return lst
Insert_sort(l)
