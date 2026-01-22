import sys
import heapq
input = sys.stdin.readline

# 방향: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(n, cave):
    INF = int(1e9)
    distance = [[INF]*n for _ in range(n)]
    distance[0][0] = cave[0][0]  # 시작점 비용 포함
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))  # (비용, x, y)

    while q:
        cost, x, y = heapq.heappop(q)
        if cost > distance[x][y]:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + cave[nx][ny]
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))
    return distance[n-1][n-1]

# 입력 처리
count = 1
while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    result = dijkstra(n, cave)
    print(f"Problem {count}: {result}")
    count += 1
