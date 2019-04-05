n = int(input())
line = list(map(int,input().split()))

for i in range(1,n):
    temp = list()
    for j in range(i):
        temp.append(abs(line[i]-line[j]))
    print (min(temp),end = " ")
    print (temp.index(min(temp))+1) 
