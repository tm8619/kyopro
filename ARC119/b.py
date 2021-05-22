n = int(input())
s = input()
t = input()
if s.count("0") != t.count("0"):
    print(-1)
else:
    ans = 0
    s = list(s)
    t = list(t)

    for i in range(n):
        if s[i] == "0":
            sindex.append(i)
            tindex.append(i)

    for i in range(n):
        if sindex[i] == tindex[i]:
            continue
        if sindex[i] > tindex[i]:
            ans += 1
            sindex[i] = tindex[i]
        else:
            break

    for i in range(n-1, -1, -1):
        if sindex[i] == tindex[i]:
            continue
        if sindex[i] < tindex[i]:
            sindex[i] = tindex[i]
            ans += 1
        else:
            break

    if sindex == tindex:
        print(ans)
    else:
        print(-1)

    sindex.reverse()
    tindex.reverse()
    for i in range(n):
        if s[i] == t[i]:
            if s[i] == "0":
                sindex.pop()
                tindex.pop()
            continue
        else:
            if s[i] == "1":
                ind = sindex.pop()
                ans += 1
                tindex.pop()
            else:
                ind = tindex[-1]
