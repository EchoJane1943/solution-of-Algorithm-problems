# 给定一个数组，奇数排左边，偶数排右边

def sortoddeven(arr):
    n = len(arr)
    for _ in range(n-1):
        for i in range(n-1):
            if arr[i]%2==0 and arr[i+1]%2==1:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

arr = [1,2,3,4,5,6,7,8,9,21,22,65,63]
sortoddeven(arr)
