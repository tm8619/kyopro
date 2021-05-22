ans = []
for i in range(1, 1000000):
    tmp = []
    for j in range(1, int(i**(1/2))+1):
        if i % j == 0:
           tmp.append(i//j)
           tmp.append(j)
    tmp.sort()
    ans.append(tmp)

input()
