n = int(input())

member = [list(map(int, input().split())) for i in range(n)]

left = 0
right = 10**18+1

while right - left > 1:
    mid = left + (right - left)//2
    ok = [0]*32
    for i in range(n):
        v = []
        for j in range(5):
            if member[i][j] >= mid:
                v.append("1")
            else:
                v.append("0")

        ok[int("".join(v),2)] = 1

    ok_flag = 0
    for i in range(1, 32):
        for j in range(i+1, 32):
            for k in range(j+1, 32):
                flag = 0
                if ok[i] == 1:
                    flag = flag | i
                if ok[j] == 1:
                    flag = flag | j
                if ok[k] == 1:
                    flag = flag | k

                if flag == 31:
                    ok_flag = 1

    if ok_flag == 1:
        left = mid
    else:
        right = mid

print(left)
