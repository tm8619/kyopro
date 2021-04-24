from collections import deque
n = int(input())

g = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

inf = 10**9
d = [-1]*(n+1)
q = deque([1])
d[1] = 0
while q:
    now = q.popleft()
    for next in g[now]:
        if d[next] == -1:
            d[next] = d[now] + 1
            q.append(next)

u = d.index(max(d))
d = [-1]*(n+1)
q = deque([u])
d[u] = 0
while q:
    now = q.popleft()
    for next in g[now]:
        if d[next] == -1:
            d[next] = d[now] + 1
            q.append(next)

print(max(d)+1)
