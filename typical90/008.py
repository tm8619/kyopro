n = int(input())
s = input()
S = list("atcoder ")
mod = 10**9+7
dp = [[0 for i in range(8)] for j in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod
        if s[i] == S[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod

print(dp[n][7])
