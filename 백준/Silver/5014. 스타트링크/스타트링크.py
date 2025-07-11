import sys
from collections import deque
input = sys.stdin.readline

def solution():
    F, S, G, U, D = map(int, input().split())
    
    def bfs(S):
        q = deque([(S, 0)])
        visited = [False] * (F + 1)
        visited[S] = True

        while q:
            now, button = q.popleft()

            if now == G:
                print(button)
                return True

            up = now + U
            down = now - D

            if 1 <= up <= F and not visited[up]:
                visited[up] = True
                q.append((up, button + 1))

            if 1 <= down <= F and not visited[down]:
                visited[down] = True
                q.append((down, button + 1))

        return False

    if not bfs(S):
        print("use the stairs")

solution()
