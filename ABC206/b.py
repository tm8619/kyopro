n = int(input())
ans = 0
for i in range(1, 1000000):
    ans += i
    if n <= ans:
        print(i)
        break
