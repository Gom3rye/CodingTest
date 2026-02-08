from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    l = deque([])
    r = deque([])
    for i in s:
        if l and i == '-':
            l.pop()
        elif l and i == '<':
            r.appendleft(l.pop())
        elif r and i == '>':
            l.append(r.popleft())
        elif i != '<' and i != '>' and i != '-':
            l.append(i)

    print(''.join(l + r))