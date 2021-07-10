n = int(input())
l = []
for i in range(n):
    t, a, b = map(int, input().split())
    if t == 1:
        l.append((a, b))
    elif t == 2:
        l.append((a, b-0.1))
    elif t == 3:
        l.append((a+0.1, b))
    else:
        l.append((a+0.1, b-0.1))

ans = 0
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[j][0] <= l[i][1] and l[i][0] <= l[j][1]:
            ans += 1
        elif l[i][0] <= l[j][1] and l[j][0] <= l[i][1]:
            ans += 1

print(ans)
