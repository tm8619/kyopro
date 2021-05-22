from bisect import *
n, k = map(int, input().split())

#まず合計値
s = [0, 0, 0, 1]
for i in range(1, 3*n+10):
    s.append(min((i+2)*(i+1)//2, (3*n+3-i)*(3*n+2-i)//2))

for i in range(len(s)-1):
    s[i+1] += s[i]

t = bisect_left(s, k)
k -= s[t-1]

for i in range(1, n+1):
    r = t-i
    if k > min(2*n+1-r, r-1):
        k -= min(2*n+1-r, r-1)

    else:
        a = i
        break

print(k)
for i in range(1, n+1):
    if max(i, t-a-i) > n:
        continue
    else:
        k -= 1
        if k == 0:
            b = i
            c = t-a-b
            break

print(k)
print(a, b, c)
