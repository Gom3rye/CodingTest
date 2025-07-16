import sys
input = sys.stdin.readline
import heapq
def solution():
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(n)]
    # 흰 방(1) 은 가중치 0, 검은 방(0) 은 가중치 1 => 0-1 BFS 또는
    # 가중치가 다른 최단 거리 => dijkstra
    INF = int(1e9)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def dijkstra(x,y):
        q = []
        distance = [[INF]*n for _ in range(n)]
        heapq.heappush(q, (0, x, y)) # cost, x, y
        distance[x][y] = 0
        while q:
            dist, x, y = heapq.heappop(q)
            if dist > distance[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<n:
                    cost = dist + (1 if maze[nx][ny]==0 else 0)
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(q, (cost, nx, ny))
        return distance[n-1][n-1]
    print(dijkstra(0,0))
solution()