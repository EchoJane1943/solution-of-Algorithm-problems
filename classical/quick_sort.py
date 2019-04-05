'''
快速排序是C.R.A.Hoare于1962年提出的一种划分交换排序。由于其采用了一种分治的策略，故称之为分治法（Divide-and-ConquerMethod）

基本思想：
1）先从数列中取出一个数作为基准数
2）分区过程，将比这个数大的数全放到它的右边，小于或者等于它的数全放到它的左边
3）再对左右区间重复第二步，直到各区间只有一个数

步骤：
1）i = L，j = R，将基准数挖出形成第一个坑a[i]
2）j –由后向前找比它小的数，找到后挖出该数，填到前一个坑a[i]中
3）i++由前向后找比它大的数，找到后挖出该数，填到坑a[j]中
4）再重复执行2，3步直到i==j，将基准数填到a[i]中
'''
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
