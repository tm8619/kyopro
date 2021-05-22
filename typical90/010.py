n = int(input())
one = [0]
two = [0]

for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        one.append(p)
        two.append(0)
    else:
        one.append(0)
        two.append(p)

for i in range(n):
    one[i+1] += one[i]
    two[i+1] += two[i]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(one[r]-one[l-1], two[r]-two[l-1])
