n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(m)]
l.sort()


ok = [True]*(2**n)
for i in range(2**n):
    bitcount = bin(i).count("1")
    for x, y, z in l:
        if bitcount == x and bin(i >> (n-y)).count("1") > z:
            ok[i] = False
            break

dp = [0]*(2**n)
dp[0] = 1
for s in range(2**n):
    if not ok[s]:
        continue
    for j in range(n):
        if s & (1 << j) == 0:
            dp[s|(1<<j)] += dp[s]

print(dp[2**n-1])
