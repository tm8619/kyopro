import random
import sys
n = int(input())

if n == 1:
    print(1)
    print(1)
    sys.exit()

fibo = [1, 1]
for i in range(150):
    fibo.append((fibo[-2]+fibo[-1]))

for i in range(140):
    if n <= fibo[i]:
        r = fibo[i-1]/fibo[i]
        break

r = (1+5**(1/2))/2-1
i = 0
while True:
    i += 1
    x = n
    y = int(x * r) + i
    if x < 0 or y < 0:
        continue

    ans = []
    for _ in range(131):
        if x == y == 0:
            break

        if x == 0:
            y -= 1
            ans.append(2)

        elif y == 0:
            x -= 1
            ans.append(1)

        elif x > y:
            x -= y
            ans.append(3)

        elif x <= y:
            y -= x
            ans.append(4)

    if len(ans) == 131:
        continue
    ans.reverse()
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])
    break
10**18
