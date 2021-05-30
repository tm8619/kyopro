n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(2*n):
    b.append((a[i], i))

b.sort()
x = []
y = []
for i in range(n):
    x.append(b[i][1])
    y.append(b[i+n][1])
x.sort()
y.sort()

ans = [None]*(2*n)
for i in range(n):
    if x[i] < y[i]:
        ans[x[i]] = "("
        ans[y[i]] = ")"
    else:
        ans[x[i]] = ")"
        ans[y[i]] = "("

print("".join(ans))
