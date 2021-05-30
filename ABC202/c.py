n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

x = [0]*(n+1)
y = [0]*(n+1)

for i in range(n):
    x[a[i]] += 1

for i in range(n):
    y[b[c[i]-1]] += 1

ans = 0
for i in range(1, n+1):
    ans += x[i]*y[i]

print(ans)
