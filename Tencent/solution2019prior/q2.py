def plan(t):
    count = 0
    if len(t) < 3:
        return 0
    if t[0] < t[1] and t[0] < t[2]: # 爬一层最好
        count += t[0]
        return count + plan(t[1:])
    if t[1] <= t[0] and t[1] < t[2]: # 跳一层最好
        count += t[1]
        return count + plan(t[2:])
    if t[2] <= t[0] and t[2] <= t[1]: # 跳两层最好
        count += t[2]
        return count + plan(t[3:])

n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))
print(plan(l))
