l, r = map(int, input().split())
# Python3 program to find prime factorization
# of a number n in O(Log n) time with
# precomputation allowed.
import math as mt
from collections import Counter
MAXN = 1000001

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

sieve()

def prime(n):
    li=[int(x) for x in range(3,n+1,2)]
    pri=[2]
    for i in range(n):
        if pri[-1]**2>n:
            pri+=li
            break
        else:
            pri.append(li[0])
            li=[int(x) for x in li if x%pri[-1]!=0]
        if len(li)==0:
            break
    return pri

primelist = prime(1000001)

d = dict()
dp = dict()
def f(x):
    ans = 0
    x = 18
    for p in primelist:
        n = x//p
        dp[p] = dict()
        dp[p][0] = 0
        for i in range(1, n+1):
            tmp = n
            tmp -= n//i

            if i in d:
                a = d[i]
            else:
                a = 1
                for key, val in Counter(getFactorization(i)).items():
                    a *= val+1
                a -= 1
                d[i] = a

            tmp -= a
            ans += tmp

            dp[p][i] = tmp + dp[p][i-1]

        for j in primelist:
            if j == p:
                break

            ans -= dp[j][n//j]
        print(dp)
        print(p, ans)
    return ans

print(f(r))


import math
def f2(x):
    ans = 0
    for i in range(1, x+1):
        for j in range(1, x+1):
            a = math.gcd(i, j)
            if a != 1:
                if i != a and j != a:
                    ans += 1
    return ans

print(f(r))
