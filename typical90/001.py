n, l = map(int, input().split())
k = int(input())
a = [0] + list(map(int, input().split())) + [l]
b = [a[i+1] - a[i] for i in range(n+1)]

left = 0
right = 10**9
while right - left > 1:
    mid = left + (right-left) // 2
    x = 0
    tmp = 0

    for i in range(n+1):
        if tmp + b[i] < mid:
            tmp += b[i]
        else:
            tmp = 0
            x += 1

    if x >= k+1:
        left = mid
    else:
        right = mid

print(left)
