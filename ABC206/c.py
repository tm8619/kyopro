from collections import Counter
n = int(input())
a = list(map(int, input().split()))

a = Counter(a)
a = a.most_common()
ans = n*(n-1)//2

for key, val in a:
    if val >= 2:
        ans -= val*(val-1)//2

print(ans)
