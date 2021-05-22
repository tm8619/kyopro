from collections import deque
s = input()

ans = deque()
f = 0
for i in range(len(s)):
    if s[i] == "R":
        f = f^1
    else:
        if f == 0:
            ans.append(s[i])
            if len(ans) >= 2:
                if ans[-1] == ans[-2]:
                    ans.pop()
                    ans.pop()
        else:
            ans.appendleft(s[i])
            if len(ans) >= 2:
                if ans[0] == ans[1]:
                    ans.popleft()
                    ans.popleft()

if f == 1:
    ans.reverse()

print("".join(map(str, ans)))
