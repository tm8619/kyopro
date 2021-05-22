n = int(input())
a = list(map(int, input().split()))

m = [0]*200
for i in range(n):
    m[a[i]%200] += 1

ans = 0
for i in range(200):
    ans += m[i]*(m[i]-1)//2

print(ans)
