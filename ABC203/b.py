n, k = map(int, input().split())
ans = 0
for i in range(n):
    for j in range(k):
        ans += int(str(i+1)+"0"+str(j+1))

print(ans)
