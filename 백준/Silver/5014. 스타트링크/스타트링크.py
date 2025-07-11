from collections import deque
import sys
input = sys.stdin.readline

def solution():
    F, S, G, U, D = map(int, input().split())
    visited = [False] * (F + 1)

    def bfs(start):
        queue = deque([(start, 0)])
        visited[start] = True

        while queue:
            floor, presses = queue.popleft()
            if floor == G:
                return presses

            # 이동 가능 시 처리
            for next_floor in (floor + U, floor - D):
                if 1 <= next_floor <= F and not visited[next_floor]:
                    visited[next_floor] = True
                    queue.append((next_floor, presses + 1))

        return -1  # 도달 불가능

    result = bfs(S)
    print(result if result != -1 else "use the stairs")

solution()