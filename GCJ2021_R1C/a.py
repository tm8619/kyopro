t = int(input())
for z in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    q = [0] + p[:] + [k+1]
    ans = 0
    for i in range(n+1):
        ans = max(ans, q[i+1]-q[i]-1)

    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                continue
            tmp = 0
            if i == 0 or i == n:
                tmp += q[i+1] - q[i] - 1
            else:
                a = q[i+1] - q[i]
                a //= 2
                tmp += a

            if j == 0 or j == n:
                tmp += q[j+1] - q[j] - 1
            else:
                a = q[j+1] - q[j]
                a //= 2
                tmp += a
            ans = max(ans, tmp)


    print("Case #{}:".format(z+1), ans/k)
