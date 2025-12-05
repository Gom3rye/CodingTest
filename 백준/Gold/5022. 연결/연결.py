import sys
from collections import deque
input = sys.stdin.readline
def solution():
    # 필요한 전선의 길이의 최솟값
    n, m = map(int, input().split()) # <=100
    # col: n, row: m
    a1c, a1r = map(int, input().split())
    a2c, a2r = map(int, input().split())
    b1c, b1r = map(int, input().split())
    b2c, b2r = map(int, input().split())
    # 정답: min(a를 미리 연결하고(장애물 취급) b를 연결, b를 미리 연결하고 a를 연결)
    # 장애물로 표시해줘야 함 -> 경로 역추적해서 배열에 표시하기
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    INF = float('inf')
    def mark_obstacles(sx, sy, ex, ey, distance, path):
        # path 배열을 역추적해서 ex, ey -> sx, sy로 가는 경로 전체를 다음 bfs의 장애물로 설정한다.
        while True:
            distance[ey][ex] = 1
            if (ex, ey) == (sx, sy):
                break
            ex, ey = path[ey][ex]

    def bfs(sx, sy, ex, ey, distance, path):
        q = deque([(sx, sy)])
        distance[sy][sx] = 0
        while q:
            x, y = q.popleft()
            if (x, y) == (ex, ey):
                return distance[y][x]
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<=n and 0<=ny<=m and distance[ny][nx] == -1:
                    distance[ny][nx] = distance[y][x]+1
                    path[ny][nx] = (x, y)
                    q.append((nx, ny))
        # 불가능할 경우 무한대 반환
        return INF
    
    def get_distance(first1c, first1r, first2c, first2r, second1c, second1r, second2c, second2r):
        distance = [[-1]*(n+1) for _ in range(m+1)] # 거리 체크 & 중복 방문 처리
        path = [[(0,0) for _ in range(n+1)] for _ in range(m+1)]
        # 나중에 그을 점들 표시해놓기 
        distance[second1r][second1c] = 0
        distance[second2r][second2c] = 0
        # 처음 2점의 거리 계산
        first_dist = bfs(first1c, first1r, first2c, first2r, distance, path)
        if first_dist >= INF:
            return INF
        
        distance = [[-1]*(n+1) for _ in range(m+1)] # 거리 체크 & 중복 방문 처리
        mark_obstacles(first1c, first1r, first2c, first2r, distance, path)
        second_dist = bfs(second1c, second1r, second2c, second2r, distance, path)
        if second_dist >= INF:
            return INF
        return first_dist+second_dist

    a_then_b = get_distance(a1c, a1r, a2c, a2r, b1c, b1r, b2c, b2r)
    b_then_a = get_distance(b1c, b1r, b2c, b2r, a1c, a1r, a2c, a2r)
    answer = min(a_then_b, b_then_a)
    print(answer if answer < INF else 'IMPOSSIBLE')
solution()