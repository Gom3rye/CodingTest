import sys
from collections import deque
input = sys.stdin.readline
def solution():
    a, b, c = map(int, input().split()) # <=500
    total = a+b+c # <=1500
    if total%3 != 0: # 3의 배수가 아니면 3개의 수가 서로 같아질 수가 없음
        print(0)
        return
    visited = [[False]*1501 for _ in range(1501)]
    a, b, c = sorted([a, b, c])
    q = deque([(a, b)])
    visited[a][b] = True
    while q:
        a, b = q.popleft()
        c = total-a-b
        if a == b == c:
            print(1)
            return
        for x, y in [(a, b), (a, c), (b, c)]:
            # 같은 수는 건들이지 않아도 됨
            if x == y:
                continue
            nx, ny = x+x, y-x
            nz = total-nx-ny
            nx, ny, nz = sorted([nx, ny, nz])
            if 0<=nx<1501 and 0<=ny<1501 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    print(0)
solution()