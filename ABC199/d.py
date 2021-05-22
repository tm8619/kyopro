import itertools
n, m = map(int, input().split())
g = [[] for i in range(n+1)]
G = [[False]*(n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

    G[a][b] = True
    G[b][a] = True

use = [False] * (n+1)

ans = 1
for i in range(1, n+1):
    if not use[i]:
        tmp = 0
        q = [i]
        v = []
        while q:
            now = q.pop()
            v.append(now)
            for next in g[now]:
                if not use[next]:
                    use[next] = True
                    q.append(next)
        for j in range(3):
            for k in itertools.product([0, 1], repeat=len(v)-1):
                a = [j]+list(k)
                print(a)
                flag = 1
                for x in range(len(v)):
                    for y in range(x+1, len(v)):
                        if a[x] == a[y]:
                            if G[x][y]:
                                flag = 0
                                break

                        if flag == 0:
                            break
                if flag == 1:
                    tmp += 1
        ans *= tmp

print(ans)
