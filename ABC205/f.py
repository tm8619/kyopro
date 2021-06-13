# Dinic's algorithm
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


h, w, n = map(int, input().split())
c = w+h+n+n+2
start = w+2*n+h
goal = w+2*n+h+1

g = Dinic(c)

for i in range(w):
    g.add_edge(start, i, 1)
for i in range(n):
    g.add_edge(w+i, w+n+i, 1)
for i in range(h):
    g.add_edge(w+n+n+i, goal, 1)

for i in range(n):
    a, b, c, d = map(int, input().split())
    a, b, c, d = a-1, b-1, c-1, d-1
    for j in range(b, d+1):
        g.add_edge(j, w+i, 1)
    for j in range(a, c+1):
        g.add_edge(w+n+i, w+n+n+j, 1)

print(g.flow(start, goal))
