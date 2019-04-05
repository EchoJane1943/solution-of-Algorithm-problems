# 腾讯2019年暑期实习生招聘提前批在线笔试技术研究和数据分析方向
# Q1 
# https://blog.csdn.net/kabuto_hui/article/details/88541781
# 问题，只能解决三个点，即n=3的情况
def minDistance(l1, l2):

    n, x0 = l1[0], l1[1]
    point = l2

    point_sorted = sorted(point)

    if x0 < point_sorted[0]:
        return point_sorted[-1] - x0
    elif x0 > point_sorted[-1]:
        return x0 - point_sorted[0]
    else:
        # 判断x0与左右两个端点之间的距离
        l = x0 - point_sorted[0]
        r = point_sorted[-1] - x0
        if l > r: # 如果左边大于右边，则去掉第一个值
            return min(r, x0 - point_sorted[1]) + point_sorted[-1] - point_sorted[1]
        else:
            return min(l, point_sorted[-2] - x0) + point_sorted[-2] - point_sorted[0]

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(minDistance(l1, l2))
