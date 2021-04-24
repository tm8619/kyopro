n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
dp = [[None]*(n+1) for i in range(64)]
for i in range(1, n+1):
    dp[0][i] = a[i]
for i in range(63):
    for j in range(1, n+1):
        dp[i+1][j] = dp[i][dp[i][j]]

k = format(k, "064b")
now = 1
for i in range(64):
    if k[i] == "1":
        now = dp[~i][now]

print(now)
