n, m, k = map(int, input().split())

mod = 10**9+7
N = 2*10**6+10
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = 0
ans += (g1[n+m]*g2[n]*g2[m])%mod
if n-k-1 >= 0:
    ans -= (g1[n+m]*g2[n-k-1]*g2[m+k+1])%mod
ans %= mod

if n-m > k:
  ans = 0

print(ans)
