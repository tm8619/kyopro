n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7

fibo = [1, 1]
for i in range(100100):
    fibo.append((fibo[-2]+fibo[-1])%mod)

mod = 10**9+7
ans = a[0]*fibo[n]
ans %= mod

for i in range(1, n):
    ans += fibo[i]*fibo[n-i]*a[i]
    ans -= fibo[i-1]*fibo[n-i-1]*a[i]
    ans %= mod

print(ans)
