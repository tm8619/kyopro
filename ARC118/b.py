k, n, m = map(int, input().split())
a = list(map(int, input().split()))


ans = []
for i in range(k):
    ans.append(m*a[i]//n)

b = []
for i in range(k):
    b.append([n*ans[i]-m*a[i], i])

b.sort()

m -= sum(ans)
for i in range(m):
    ans[b[i][1]] += 1

print(" ".join(map(str, ans)))
