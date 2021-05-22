T = int(input())
def f(t, p):
    if t == 0 and p >= 3:
        return 0

    ret = -1
    for i in range(3, min(p, t+1)):
        if p % i == 0:
            if t-p//i >= 0 and p//i >= 3:
                ret = max(ret, f(t-p//i, p//i))
    print(t, p, ret)
    return ret + 1

for z in range(T):
    n = int(input())
    ans = 0

    for j in range(3, n):
        ans = max(ans, f(n, j))
    print("Case #{}:".format(z+1), ans)
