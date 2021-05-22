t = int(input())
for z in range(t):
    x = int(input())
    if x >= 998999:
        print("Case #{}:".format(z+1), 1234567)
        continue
    x += 1
    ans = -1
    while True:
        x = str(x)
        for i in range(1, 4):
            if len(x) < 2*i:
                break

            k = int(x[:i])
            for j in range(1, 7//i+1):
                if "".join(map(str, [k+a for a in range(j)])) == x:
                    ans = int(x)
                    break
            if ans != -1:
                break

        if ans != -1:
            break

        x = int(x) + 1

    print("Case #{}:".format(z+1), ans)
