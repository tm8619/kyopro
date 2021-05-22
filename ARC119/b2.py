n = int(input())
s = input()
t = input()
if s.count("0") != t.count("0"):
    print(-1)
else:
    ans = 0
    s = list(s)
    t = list(t)
    sindex = []
    tindex = []
    for i in range(n):
        if s[i] == "0":
            sindex.append(i)
        if t[i] == "0":
            tindex.append(i)
    m = len(sindex)
    for i in range(m):
        if sindex[i] != tindex[i]:
            ans += 1

    print(ans)
