import sys
from collections import deque
input = sys.stdin.readline

def solution():
    F, S, G, U, D = map(int, input().split())
    
    def bfs(S):
        q = deque([(S, 0)])
        visited = set([S])  # 시작층은 방문 처리

        while q:
            now, button = q.popleft()

            if now == G:
                print(button)
                return True

            up = now + U
            down = now - D

            if 1 <= up <= F and up not in visited:
                visited.add(up)
                q.append((up, button + 1))

            if 1 <= down <= F and down not in visited:
                visited.add(down)
                q.append((down, button + 1))

        return False

    if not bfs(S):
        print("use the stairs")

solution()