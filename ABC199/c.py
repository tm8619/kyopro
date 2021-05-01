
n = int(input())
s = input()
q = int(input())

s = [list(s[:n]), list(s[n:])]

import sys
input = sys.stdin.readline
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        s[(a-1)//n][(a-1)%n], s[(b-1)//n][(b-1)%n] = s[(b-1)//n][(b-1)%n], s[(a-1)//n][(a-1)%n]

    else:
        s[0], s[1] = s[1], s[0]

print("".join(map(str, s[0])) + "".join(map(str, s[1])))
