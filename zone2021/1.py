n, m = map(int, input().split())

maxi = 0
g = [set([i]) for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if maxi < len(g[i]|g[j]|g[k]):
                ans = (i, j, k)
                maxi = len(g[i]|g[j]|g[k])
print(ans)
