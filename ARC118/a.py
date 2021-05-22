t, n = map(int, input().split())

m = set()
for i in range(1, 101):
    m.add(i*(100+t)//100)

m = set([i for i in range(1, 100+t)]) - m
m = list(m)
m.sort()

k = (n-1) % len(m)
l = (n-1) // len(m)
print(m[k] + (100+t)*l)
