n = int(input())
a = list(map(int, input().split()))

#dp[i][j] [i, j]が抜けるために必要な最小コスト
dp = [[10**18 for i in range(2*n)] for j in range(2*n)]

for i in range(2*n):
    dp[i][i] = 0

for i in range(2*n-1):
    dp[i][i+1] = abs(a[i]-a[i+1])

for d in range(3, 2*n, 2):
    for i in range(2*n):
        j = i+d
        if j >= 2*n:
            continue
        dp[i][j] = min(dp[i][j], dp[i+1][j-1] + abs(a[i]-a[j]))
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
print(dp[0][-1])
