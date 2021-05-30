a, b, k = map(int, input().split())

ans = []
g = [1]
for i in range(1, 61):
    g.append(g[-1]*i)

for _ in range(a+b):
    if a == 0:
        ans.append("b")
        b -= 1
        continue
    if b == 0:
        ans.append("a")
        a -= 1
        continue

    r = g[a-1+b]//g[a-1]//g[b]
    if k <= r:
        ans.append("a")
        a -= 1
        continue

    else:
        ans.append("b")
        b -= 1
        k -= r
        continue

print("".join(ans))
