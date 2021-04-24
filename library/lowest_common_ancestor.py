import sys
input = sys.stdin.readline
n = int(input())
INF = 2**31-1
class SegmentTree():
    def __init__(self, N):
        self.N0 = 2**(N-1).bit_length()
        self.data = [(INF,INF)]*((2*self.N0)+1)

    # a_k の値を x に更新
    def update(self, k, x):
        k += self.N0-1
        self.data[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])

    # 区間[l, r)の最小値
    def query(self, l, r):
        L = l + self.N0; R = r + self.N0
        s = (INF,INF)
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])

            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

human = [[] for i in range(n)]
for i in range(n):
    a = int(input())-1
    if a == -2:
        root = i
    else:
        human[i].append(a)
        human[a].append(i)

q = [root]
depth = [-1]*n
depth[root] = 0
route = []

while q:
    now = q.pop()
    if now >= 0:
        route.append(now)
        for next in human[now][::-1]:
            if depth[next] == -1:
                depth[next] = depth[now] + 1
                q.append(~now)
                q.append(next)
    else:
        route.append(~now)
for i in range(len(route)):
    route[i] = (depth[route[i]], route[i])

first = [-1]*n
for i in range(len(route)):
    now = route[i][1]
    if first[now] == -1:
        first[now] = i

segtree = SegmentTree(len(route))
for i in range(len(route)):
    segtree.update(i, route[i])


m = int(input())
q = [list(map(int, input().split())) for i in range(m)]
for a, b in q:
    a_i, b_i = first[a-1], first[b-1]
    if a_i > b_i:
        a_i, b_i = b_i, a_i
    lca = segtree.query(a_i, b_i+1)[1]
    if lca == b-1:
        print("Yes")
    else:
        print("No")
