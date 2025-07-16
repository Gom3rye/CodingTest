import heapq, sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def dijkstra():
    queue = [(0,0,0)]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    while queue:
        next, nowx, nowy = heapq.heappop(queue)
        if nowx == n-1 and nowy == m-1: return next
        for i in range(4):
            nx = nowx + dx[i]
            ny = nowy + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == '1':
                    heapq.heappush(queue, (next+1, nx,ny))
                elif graph[nx][ny] == '0':
                    heapq.heappush(queue, (next,nx,ny))
print(dijkstra())