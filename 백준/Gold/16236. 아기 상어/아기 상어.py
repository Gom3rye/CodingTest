import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n = int(input())
    sea = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                sx, sy = i, j # shark의 위치
                sea[i][j] = 0 # 상어 위치는 빈칸으로 초기화
                break

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    # 먹을 수 있는 최단 거리의 물고기 거리와 위치 반환
    def bfs(sx, sy, size):
        distance = [[-1]*n for _ in range(n)] # 중복 방문 방지 + 거리 상태 저장
        fish = []
        distance[sx][sy] = 0
        q = deque([(sx, sy)]) # q에는 이동할 수 있는 좌표들 담으면서 최단 거리에 있는 fish_list 구하기
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<n and distance[nx][ny] == -1:
                    # 상어 크기보다 작거나 같으면 이동 가능
                    if sea[nx][ny] <= size:
                        distance[nx][ny] = distance[x][y]+1
                        q.append((nx, ny))
                        # 상어 크기보다 작으면 먹을 수 있음
                        if 0 < sea[nx][ny] < size:
                            fish.append((distance[nx][ny], nx, ny))

        return sorted(fish)
        
    time, size, ate = 0, 2, 0 # 초, 상어 크기, 먹은 물고기 개수
    while True:
        fish_list = bfs(sx, sy, size)
        if not fish_list: # 아무것도 없어서 None을 반환한다면 (무한루프 종료조건)
            break 
        dist, fx, fy = fish_list[0] # 가장 우선 순위에 있는 물고기 뽑아서 먹기
        sea[fx][fy] = 0 # 먹고 난 자리 0으로 업데이트
        time += dist
        ate += 1
        sx, sy = fx, fy # 상어 위치 상태 업데이트
        if ate == size:
            size += 1
            ate = 0
    print(time)
solution()