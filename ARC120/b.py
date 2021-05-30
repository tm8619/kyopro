h, w = map(int, input().split())
g = [list(input()) for i in range(h)]
ans = 1
s = h+w-2
mod = 998244353
for t in range(s+1):
    b = 0
    r = 0
    d = 0
    for i in range(h):
        j = t-i
        if not 0 <= j <= w-1:
            continue

        if g[i][j] == "B":
            b += 1
        elif g[i][j] == "R":
            r += 1
        else:
            d += 1

    if b == 0 and r == 0:
        ans *= 2
        ans %= mod

    elif b == 0:
        pass
    elif r == 0:
        pass
    elif b != 0 and r != 0:
        ans *= 0

print(ans)
