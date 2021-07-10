a, b, c, d = map(int, input().split())
ans = -1
for i in range(10**6):
    if a+b*i <= c*d*i:
        ans = i
        break

print(ans)
