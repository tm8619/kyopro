# 文字列を昇順・降順に並び替える関数
def str_sort(x, s = False):
    y = sorted(x, reverse = s)
    return ''.join(y)


def power_func(a,n,p):
  bi=str(format(n,"b"))
  res=1
  for i in range(len(bi)):
    res=(res*res) %p
    if bi[i]=="1":
      res=(res*a) %p
  return res

#BFS
q = queue.Queue()
q.put(1)
visit[1] = True
while (not q.empty()):
    now = q.get()
    for next in g[now]:
        if not visit[next]:
            visit[next] = True
            q.put(next)

compress2 = lambda arr: {e: i for i, e in enumerate(sorted(set(arr)))}

# 素因数分解
def factorization(N):
    prime = primelist(int(N**(1/2))+2)
    factor = [0 for i in range(int(N**(1/2)+2))]
    isprime = False
    for i in prime:
        while N % i == 0:
            N = N // i
            factor[i] += 1
    if sum(factor) == 0:
        isprime = True
    if N != 1:
        factor.append(1)
    return factor, isprime

# 素数
def primelist(N):
    prime = [2]
    for i in range(3, N+1):
        flag = 1
        for j in prime:
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            prime.append(i)
    return prime

# 素数判定
import random
def is_prime(n):
    if n == 2: return True
    if n == 1 or n & 1 == 0: return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

#combination
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


mod =
N =
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def standard_form(A):
    C = A[:]
    L = 60
    E = []
    ids = []
    for i in range(L):
        e = j0 = None
        mask = (1 << i)-1
        for j, a in enumerate(C):
            if (a >> i) & 1 and (a & mask) == 0:
                e = a
                j0 = j
                break
        else:
            continue
        ids.append(j0)
        for j, a in enumerate(C):
            if j0 == j:
                continue
            if (a >> i) & 1:
                C[j] ^= e
    return [C[e] for e in ids]
#interactive
import sys
readline = sys.stdin.readline
write = sys.stdout.write
flush = sys.stdout.flush

# クエリ: "? x1 x2" を出力
def query(x1, x2):
    write("? %d %d\n" % (x1, x2))
    flush()
    # ジャッジから返される値を取得
    return readline().strip()

# 回答: "! x" を出力
def answer(x):
    write("! %d\n" % x)
    flush()
    # 即時終了
    exit(0)




#warshall-floyd
INF = 2 ** 63 - 1
d = [[INF for i in range(N+1)] for j in range(N+1)]
for i in range(N+1):
    d[i][i] = 0
for i in range(M):
    a, b, c = map(int, input().split())
    d[a][b] = c
    d[b][a] = c
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])


#bellman-ford
INF = 2 ** 63 - 1
d = [(-1)*INF for i in range(N+1)]
for i in range(N):
    d_N = d[N]
    for j in range(M):
        a = data[j][0]
        b = data[j][1]
        c = data[j][2]
        d[b] = max(d[b], d[a]+c)
    if i == N-1:
        if d_N != d[N]:
            ans = "inf"
        else:
            ans = d[N]

#dijkstra
import heapq
queue = []
while count != n:
    now = heapq.heappop(queue)
    if check[now[1]]:
        continue
    else:
        count += 1
        check[now[1]] = True
        for path in graph[now[1]]:
            if not check[path[0]]:
                if city_yen_cost[now[1]]+path[1] < city_yen_cost[path[0]]:
                    city_yen_cost[path[0]] = city_yen_cost[now[1]]+path[1]
                    heapq.heappush(queue, [city_yen_cost[now[1]]+path[1], path[0]])
while q:
    now_c, now = heappop(q)
    for next, next_c in g[now]:
        if now_c + next_c > cost[next]:
            continue
        heappush(q, (now_c + next_c, next))
        cost[next] = min(cost[next], now_c + next_c)
    if count == n:
        break


#しゃくとり
r = 0
sum = 0
ans = 0
for l in range(N):
    while sum < K and r <= N-1:
        sum += a[r]
        r += 1

    else:
        if sum >= K:
            ans += N - r + 1
        sum -= a[l]
print(ans)

#重複を取り除く
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]


#にぶたん
while right - left > 1:
    mid = left + (right-left)//2
    if isok(mid):
        right = mid
    else:
        left = mid


#pypy使う
from subprocess import*
cmd=['pypy3','-c',"""

"""]
call(cmd)

#レーベンシュタイン距離
def get_levenshtein_distance(s1, s2, normalize = False):
    l1, l2 = len(s1), len(s2)
    #dp[i][j]: s1のi文字目までとs2のj文字目までのlevenshtein距離
    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
    for i in range(l1+1):
        dp[i][0] = i
    for j in range(l2+1):
        dp[0][j] = j

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            replacement_cost = int(not s1[i-1] == s2[j-1])
            dp[i][j] = min(dp[i-1][j] + 1,　
                           dp[i][j-1] + 1,
                           dp[i-1][j-1] + replacement_cost)

    if normalize:
        return dp[l1][l2] // max(l1, l2)
    return dp[l1][l2]

def max_subarray(arr):
    max_ending = max_current = arr[0]
    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)
    return max_current



#転倒数
def inversion(a):
    ans = 0
    for i, p in enumerate(b):
        bit.add(p, 1)
        ans += i+1 - bit.sum(p)
    return ans


# Python3 program to find prime factorization
# of a number n in O(Log n) time with
# precomputation allowed.
import math as mt

MAXN = 100001

# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]

# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):

        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i

    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):

        # checking if i is prime
        if (spf[i] == i):

            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):

                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i

# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step
def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]

    return ret

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

a = factorization(n)
A からスタートして、D を足していくとき、個数 mod B の最大は，g = gcd(B, D) として B−g+(A mod g)
となり，これを C と比較すればよいです。個数 mod g が常に一定であることを考えるとこれが上界であるこ
とは言え、また，(B/g − 1) × inv(D/g, B/g) 回 D を足したときにこの上界が達成できます (inv(X, Y ) は，
X × inv = 1 mod Y なる値とします)。



#座標圧縮
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}
compress3 = lambda arr: list(map({e: i for i, e in enumerate(sorted(set(arr)))}.__getitem__, arr))
