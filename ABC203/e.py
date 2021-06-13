n, m = map(int, input().split())
ok = [False]*(500000)
ok[0] = True
p = [list(map(int, input().split())) for i in range(m)]
d = dict()
for x,y in p:
    if x not in d:
        d[x] = [y]
    else:
        d[x].append(y)

q = []
for key, val in d.items():
    q.append((key, val))

q.sort()

for _, key in q:
    ok_y = []
    for y in key:
        y -= n
        if not -200001 <= y <= 200001:
            continue

        if ok[y-1] or ok[y+1]:
            ok_y.append(y)

    for y in key:
        y -= n
        if not -200001 <= y <= 200001:
            continue
        ok[y] = False
        
    for y in ok_y:
        ok[y] = True

print(sum(ok))
