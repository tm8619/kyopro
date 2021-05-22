n, D, H = map(int, input().split())
ans = 0
for i in range(n):
    d, h = map(int, input().split())
    ans = max(ans, h-(d*(H-h)/(D-d)))

print(ans)
