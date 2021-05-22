from collections import *

n, k = map(int, input().split())
s = input()

index = [deque([]) for i in range(26)]
for i in range(n):
    index[ord(s[i])-97].append(i)

ans = []

c = k
now = 0
for i in range(k):
    for j in range(26):
        while len(index[j]) > 0 and index[j][0] < now:
            index[j].popleft()
        if len(index[j]) == 0:
            continue
            
        if index[j][0] <= n-c and index[j][0] >= now:
            x = index[j].popleft()
            ans.append(chr(j+97))
            c -= 1
            now = x
            break


print("".join(map(str, ans)))
