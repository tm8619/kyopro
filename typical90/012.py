class Union_Find():
    def __init__(self, num):
        self.par = [-1]*(num+1)
        self.siz = [1]*(num+1)

    def same_checker(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        while self.par[x] >= 0:
            if self.par[self.par[x]] >= 0:
                self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] < self.par[ry]:
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.siz[ry] += self.siz[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
        return

    def size(self, x):
        return self.siz[self.find(x)]

h, w = map(int, input().split())
g = [[False for i in range(w+2)] for j in range(h+2)]
Q = int(input())

tree = Union_Find(5000000)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        g[q[1]][q[2]] = True
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if g[q[1]+dx][q[2]+dy]:
                tree.union(q[1]*2000+q[2], (q[1]+dx)*2000+(q[2]+dy))

    else:
        if tree.same_checker(q[1]*2000+q[2], q[3]*2000+q[4]) and g[q[1]][q[2]] and g[q[3]][q[4]]:
            print("Yes")
        else:
            print("No")
