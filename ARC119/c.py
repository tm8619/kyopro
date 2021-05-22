from collections import Counter
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i % 2 == 1:
        a[i] *= -1

s = [0]
for i in range(n):
    s.append(s[-1]+a[i])

s = Counter(s)
s = s.most_common()
ans = 0
for _, v in s:
    if v >= 2:
        ans += v*(v-1)//2

print(ans)
