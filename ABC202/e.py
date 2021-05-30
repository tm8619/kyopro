import sys
sys.setrecursionlimit(1000000)
n = int(input())
p = list(map(int, input().split()))

g = [[] for i in range(n+1)]
for i in range(n-1):
    g[p[i]].append(i+2)

memo = dict()

dist = [0]*(n+1)
q = [1]
while q:
    now = q.pop()
    for next in g[now]:
        dist[next] = dist[now] + 1
        q.append(next)

def rec(now, d):
    if dist == 0:
        return 1

    if (now, d) in memo:
        return memo[(now, d)]

    ret = 0
    for next in g[now]:
        ret += rec(next, d-1)

    memo[(now, d)] = ret
    return ret

q = int(input())
q = 100000
for i in range(q):
    u, d = map(int, input().split())
    if dist[u] > d:
        print(0)
        continue

    print(rec(u, d-dist[u]))
