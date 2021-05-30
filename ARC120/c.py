import sys
from collections import deque
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

class BIT():
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

def inversion(a):
    ans = 0
    for i, p in enumerate(a):
        bit.add(p, 1)
        ans += i+1 - bit.sum(p)
    return ans

for i in range(n):
    a[i] += i
    b[i] += i

if sorted(a) != sorted(b):
    print(-1)
    sys.exit()

d = dict()
for i in range(n):
    if b[i] not in d:
        d[b[i]] = deque([i+1])
    else:
        d[b[i]].append(i+1)

for i in range(n):
    a[i] = d[a[i]].popleft()



bit = BIT(n)
print(inversion(a))
