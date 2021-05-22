import math
from bisect import *
n = int(input())
p = [list(map(int, input().split())) for i in range(n)]

math.atan2(0, 0)


ans = 0
for i in range(n):
    xi, yi = p[i]
    arg = []
    for j in range(n):
        if i == j:
            continue
        xj, yj = p[j]
        arg.append(math.atan2(yj-yi, xj-xi)*180/math.pi + 180)
    arg.append(-10**9)
    arg.append(10**9)
    arg.sort()
    for j in range(1, n):
        index = bisect_left(arg, arg[j]+180)
        ans = max(ans, min((arg[index]-arg[j]), 360-(arg[index]-arg[j])))
        ans = max(ans, min((arg[index-1]-arg[j])%180, 360-(arg[index-1]-arg[j])))
print(ans)
