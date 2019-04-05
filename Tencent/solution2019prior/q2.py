def printNum(n):

    num = [i for i in range(1, n+1)]

    while n > 1:
        print(num[0], '', end='')
        num = num[2:] + [num[1]]
        n -= 1
    print(num[0])

if __name__ == '__main__':
    n = int(input())
    printNum(n)
