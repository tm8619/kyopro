from heapq import *
r, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]
b = [list(map(int, input().split())) for i in range(r-1)]

cost = [[10**18 for i in range(c)] for j in range(r)]

q = []

visit = [[False for i in range(c)] for j in range(r)]

heappush(q, (0, (0, 0)))


while q:
    now_c, now = heappop(q)
    if now == (r-1, c-1):
        break
    now_x = now[0]
    now_y = now[1]
    if visit[now_x][now_y]:
        continue
    visit[now_x][now_y] = True

    if now_y < c-1:
        C = a[now_x][now_y]
        if now_c + C <= cost[now_x][now_y+1]:

            cost[now_x][now_y+1] = now_c + C
            heappush(q, (now_c+C, (now_x, now_y+1)))

    if now_y > 0:
        C = a[now_x][now_y-1]
        if now_c + C <= cost[now_x][now_y-1]:


            cost[now_x][now_y-1] = now_c + C
            heappush(q, (now_c+C, (now_x, now_y-1)))

    if now_x < r-1:
        C = b[now_x][now_y]
        if now_c + C <= cost[now_x+1][now_y]:


            cost[now_x+1][now_y] = now_c + C
            heappush(q, (now_c+C, (now_x+1, now_y)))



    if now_x > 0:
        C = 2
        if now_c + C <= cost[now_x-1][now_y]:
            cost[now_x-1][now_y] = now_c + C
            heappush(q, (now_c+C, (now_x-1, now_y)))



print(cost[r-1][c-1])
