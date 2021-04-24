h, w = map(int, input().split())

a = [list(map(int, input().split())) for i in range(h)]
b = []
c = []
for i in range(h):
    s = 0
    for j in range(w):
        s += a[i][j]
    b.append(s)

for i in range(w):
    s = 0
    for j in range(h):
        s += a[j][i]
    c.append(s)

ans = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = b[i] + c[j] - a[i][j]

for i in range(h):
    print(*ans[i])
