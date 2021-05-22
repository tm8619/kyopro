n = int(input())

ans = []
for i in range(1, 10001):
    if i == 12:
        continue
    if i % 6 == 0 or i % 10 == 0 or i % 15 == 0:
        ans.append(i)

print(" ".join(map(str, ans[:n])))
