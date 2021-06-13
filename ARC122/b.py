n = int(input())
a = list(map(int, input().split()))

def f(x):
    lose = 0
    for i in range(n):
        lose += (x+a[i]-min(a[i], 2*x))
    return lose

high = 10**10
low = 0
for _ in range(100):
    mid_left = high/3+low*2/3
    mid_right = high*2/3+low/3
    if f(mid_left) >= f(mid_right):
        low = mid_left
    else:
        high = mid_right


print(f(high)/n)
