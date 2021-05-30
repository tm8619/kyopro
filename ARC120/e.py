n = int(input())
a = list(map(int, input().split()))


left = 0
right = 10**9
while right - left > 1:
    k = left + (right - left) // 2
    flag = 1
    for i in range(n//2):
        if not a[2*i+1] - a[2*i] <= 2 * k:
            flag = 0

        if i != n//2 - 1:
            if not a[2*i] + k >= a[2*i+3] - k:
                flag = 0
    if n % 2 == 1:
        if not a[-3] + k >= a[-1] - k:
            flag = 0

    if n % 2 == 1 and flag == 0:
        flag = 1
        for i in range(n//2):
            if not a[2*i+2] - a[2*i+1] <= 2 * k:
                flag = 0

            if 2*i+4 >= n:
                continue

            if not a[2*i+1] + k >= a[2*i+4] - k:
                flag = 0
                
        if not a[0] + k >= a[2] - k:
            flag = 0

    if flag == 1:
        right = k
    else:
        left = k

print(right)
