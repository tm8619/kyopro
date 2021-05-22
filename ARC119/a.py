n = int(input())
ans = 10**18
for i in range(80):
    a = n // 2**i
    c = n % 2**i
    b = i
    ans = min(ans, a+b+c)
print(ans)
