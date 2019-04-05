def quick_sort(li, start, end):
    # 递归结束条件：
    if start >= end:
        return
    # 左边第一个索引
    left = start
    # 右边最后一个索引
    right = end
    # 把第一个数作为中间值
    mid = li[left]
    # 首先右边的索引往左移动，当left<right 的时候和right的值大于mid值时才执行循环
    while left < right:
        while left < right and li[right] >= mid:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= mid:
            left += 1
        li[right] = li[left]
    li[left] = mid
    # 此时，mid左边的数都小于mid， mid右边的数都大于mid
    # 将两边的数再通过递归的方式进行排序
    quick_sort(li, start, left - 1)
    quick_sort(li, left + 1, end)


if __name__ == '__main__':
    li = [4, 3, 88,1,5, 7]
    quick_sort(li, 0, len(li) - 1)
    print(li)
