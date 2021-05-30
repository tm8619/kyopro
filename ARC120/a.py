n = int(input())
a = list(map(int, input().split()))
maxi = [a[0]]
s = [a[0]]
for i in range(n-1):
    s.append(a[i+1]+s[i])
for i in range(n-1):
    maxi.append(max(a[i+1], maxi[i]))

ans = 0
for i in range(n):
    ans += maxi[i]*(i+1) + s[i]
    print(ans)
    ans -= maxi[i]*(i+1)
