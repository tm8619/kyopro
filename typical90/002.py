n = int(input())

ans = []
for i in range(2**n):
    b = format(i, "0{}b".format(n))
    k = 0
    for j in range(n):
        if b[j] == "0":
            k += 1
        else:
            k -= 1
        if k < 0:
            k = 10**9
            break
    if k == 0:
        ans.append(b.replace("0", "(").replace("1", ")"))

for i in ans:
    print(i)
