from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
q = int(input())

a.append(-10**18)
a.append(10**18)
a.sort()
for _ in range(q):
    x = int(input())
    ind = bisect_left(a, x)
    print(min(a[ind]-x, x-a[ind-1]))
