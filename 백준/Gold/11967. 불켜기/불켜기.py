import sys
from collections import deque, defaultdict
input = sys.stdin.readline
INF = float('inf')
def solution():
    # 불을 켤 수 있는 방의 최대 개수 구하기
    n, m = map(int, input().split()) # 보드 사이즈 <=100, #스위치 <=20000
    graph = defaultdict(set)
    for _ in range(m):
        x, y, a, b = map(int, input().split())
        graph[(x-1,y-1)].add((a-1,b-1)) # (x,y)->(a,b)로 갈 수 있다. 0based index
    # 불이 켜져 있는 곳과 내가 방문 가능한 곳을 따로 관리해야 한다. (1,3에 불이 켜져 있어도 상하좌우밖에 이동 못하니까 내가 1,1이라면 이동 못하기 때문)
    lights = [[False]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True
    lights[0][0] = True # (0,0)은 불 켜져있고 이동할 수 있다.
    cnt = 1 # 방문할 수 있는 칸의 수
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft() # 큐에 이동 가능한 곳만 넣기
        # 1. 현재 방에서 켤 수 있는 스위치 모두 켜기
        for sx, sy in graph[(x, y)]:
            if not lights[sx][sy]:
                lights[sx][sy] = True
                cnt += 1
                # 불 킨 곳 주변에 불이 켜져 있고 이미 갔던 곳이면
                for nx, ny in [(sx-1,sy),(sx+1,sy),(sx,sy-1),(sx,sy+1)]:
                    if 0<=nx<n and 0<=ny<n and lights[nx][ny] and visited[nx][ny]:
                        visited[sx][sy] = True # 이번에 새로 불 킨 곳도 갈 수 있다.
                        q.append((sx, sy))
                        break
        # 2. 현재 방에서 상하좌우 이동해보기
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and lights[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    print(cnt)
solution()
