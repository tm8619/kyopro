n = int(input())
a = list(map(int, input().split()))
a.sort()
f = 1
for i in range(n):
    if a[i] == i+1:
        continue

    f = 0
    break

if f == 1:
    print("Yes")
else:
    print("No")
