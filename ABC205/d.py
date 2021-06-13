from bisect import *
n, q = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= i

for _ in range(q):
    k = int(input())
    i = bisect_right(a, k)
    print(k+i)
    
