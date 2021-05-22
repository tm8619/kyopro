from copy import deepcopy
n = int(input())
a = list(map(int, input().split()))


m = [0]*200
for i in range(n):
    m[a[i]%200] += 1

mm = [[] for i in range(200)]
for i in range(n):
    mm[a[i]%200].append(i+1)

ansmod = -1
for i in range(200):
    if m[i] >= 2:
        ansmod = i
        break


if ansmod != -1:
    print("Yes")
    ans = []
    for i in range(n):
        if a[i] % 200 == ansmod:
            ans.append(i+1)

    print(1, ans[0])
    print(1, ans[1])

else:
    b = []
    for i in range(200):
        if m[i] == 1:
            b.append(i)


    if len(b) >= 8:
        b = b[:8]

    m = [[] for i in range(200)]
    for i in range(2**len(b)):
        i = format(i, "0{}b".format(len(b)))
        tmp = 0
        for j in range(len(b)):
            if i[j] == "1":
                tmp += b[j]
        tmp %= 200
        m[tmp].append(i)

    f = 0
    for i in range(200):
        if len(m[i]) >= 2:
            ans1s = m[i][0]
            ans2s = m[i][1]
            f = 1
            break

    if f == 0:
        print("No")

    else:
        ans1 = []
        ans2 = []
        for i in range(len(b)):
            if ans1s[i] == "1":
                ans1.append(b[i])
            if ans2s[i] == "1":
                ans2.append(b[i])

        c = deepcopy(mm)
        for i in range(len(ans1)):
            x = c[ans1[i]].pop()
            ans1[i] = x

        c = deepcopy(mm)
        for i in range(len(ans2)):
            x = c[ans2[i]].pop()
            ans2[i] = x

        ans1.sort()
        ans2.sort()

        print("Yes")
        print(len(ans1), " ".join(map(str, ans1)))
        print(len(ans2), " ".join(map(str, ans2)))
