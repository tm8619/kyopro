

t = int(input())

def bit_not(num):
    if num == 0:
        return 1
    num = ~num & (1 << 16 - 1)
    return num

for z in range(t):
    S, E = input().split()
    S = int(S, 2)
    E = int(E, 2)
    if S == E:
        print("Case #{}:".format(z+1), 0)
        continue
    ans = 100
    for i in range(2**16):
        s, e = S, E
        n = i
        b = i.bit_length()
        i = format(i, "016b")

        for j in range(b):
            if i[j] == "0":
                s = bit_not(s)
            else:
                s = s*2
            if s == e:
                ans = min(ans, j+1)

            if s > 2**18:
                break

    if ans == 100:
        ans = "IMPOSSIBLE"
    print("Case #{}:".format(z+1), ans)
