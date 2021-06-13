n, k = map(int, input().split())
w = [list(map(int, input().split())) for i in range(n)]

left = 0
right = 10**9

while right - left > 1:
    mid = left + (right - left) // 2
    g = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if w[i][j] >= mid:
                g[i][j] = 1


    s = 0
    for i in range(k):
        for j in range(k):
            s += g[i][j]


    flag = 0
    if s < k**2//2 + 1:
        flag = 1

    for i in range(n-k+1):
        if i % 2 == 0:
            for j in range(n-k):
                for x in range(i, i+k):
                    s += g[x][j+k]
                    s -= g[x][j]

                if s < k**2 // 2 + 1:
                    flag = 1
                    break

            if flag == 1:
                break
        if flag == 1:
            break


        else:
            for j in range(n-k-1, -1, -1):
                for x in range(i, i+k):
                    s -= g[x][j+k]
                    s += g[x][j]

                if s < k**2 // 2 + 1:
                    flag = 1
                    break
                if flag == 1:
                    break


        if i % 2 == 0:
            if i == n-k:
                continue
            for j in range(n-k, n):
                s -= g[i][j]
                s += g[i+k][j]

            if s < k**2 // 2 + 1:
                flag = 1
                break

        else:
            if i == n-k:
                continue
            for j in range(k):
                s -= g[i][j]
                s += g[i+k][j]

            if s < k**2 // 2 + 1:
                flag = 1
                break

    if flag == 1:
        right = mid
    else:
        left = mid

print(left)
