n, k = map(int, input().split())
friend = [list(map(int, input().split())) for i in range(n)]
friend.sort()

ans = k


for i in range(n):
    if ans >= friend[i][0]:
        ans += friend[i][1]

print(ans)
