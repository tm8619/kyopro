#min
INF = 2**31-1
class SegmentTree():
    def __init__(self, N):
        self.N0 = 2**(N-1).bit_length()
        self.data = [INF]*((2*self.N0)+1)

    # a_k の値を x に更新
    def update(self, k, x):
        k += self.N0-1
        self.data[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])

    # 区間[l, r)の最小値
    def query(self, l, r):
        L = l + self.N0; R = r + self.N0
        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])

            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

#max
INF = -2**31+1
class SegmentTree():
    def __init__(self, N):
        self.N0 = 2**(N-1).bit_length()
        self.data = [INF]*((2*self.N0)+1)

    # a_k の値を x に更新
    def update(self, k, x):
        k += self.N0-1
        self.data[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.data[k] = max(self.data[2*k+1], self.data[2*k+2])

    # 区間[l, r)の最小値
    def query(self, l, r):
        L = l + self.N0; R = r + self.N0
        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = max(s, self.data[R-1])

            if L & 1:
                s = max(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s
        
# N: 処理する区間の長さ
N, Q = map(int, input().split())
segtree = SegmentTree(N)
segtree.data
#初期化:
"""
for i in range(1, N+1):
    update(i, a[i])
"""
for i in range(Q):
    q, l, r = map(int, input().split())
    if q == 1:
        print(segtree.query(l, r+1))
    else:
        segtree.update(l, r)


#1indexed
class BIT():
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

bit = [BIT(n+1) for i in range(26)]



INF = 2**63-1
class LasySegmentTree():
    def __init__(self, N):
        self.N0 = 2**(N-1).bit_length()
        self.data = [0]*(2*self.N0)
        self.lazy = [0]*(2*self.N0)

    def gindex(self, l, r):
        L = l + self.N0; R = r + self.N0
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v; self.lazy[2*i] += v
            self.data[2*i-1] += v; self.data[2*i] += v
            self.lazy[i-1] = 0

    def update(self, l, r, x):
        L = self.N0 + l; R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] += x; self.data[R-1] += x
            if L & 1:
                self.lazy[L-1] += x; self.data[L-1] += x
                L += 1
            L >>= 1; R >>= 1
        for i in self.gindex(l, r):
            self.data[i-1] = min(self.data[2*i-1], self.data[2*i]) + self.lazy[i-1]

    def query(self, l, r):
        self.propagates(*self.gindex(l, r))
        L = self.N0 + l; R = self.N0 + r

        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])
            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s



def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x

def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x

import typing
import atcoder._bit
class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = atcoder._bit._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
