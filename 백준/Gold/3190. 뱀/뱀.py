import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n = int(input()) # 보드의 크기
    k = int(input()) # 사과의 개수
    apples = set()
    for _ in range(k):
        x, y = map(int, input().split())
        apples.add((x,y))
    l = int(input()) # 뱀의 방향 변환 횟수
    dir = {}
    for _ in range(l):
        x, c = map(str, input().split())
        dir[int(x)] = c
    visited = [[False]*(n+1) for _ in range(n+1)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0] # 우, 하, 좌, 상

    # 뱀의 시작 위치 넣고 초기화
    snake = deque()
    snake.append((1, 1))
    x, y, time, d = 1, 1, 0, 0
    visited[1][1] = True

    while True:
        nx, ny = dx[d]+x, dy[d]+y
        time += 1
        if not 1<=nx<=n or not 1<=ny<=n or visited[nx][ny] == True:
            break
        visited[nx][ny] = True
        snake.append((nx, ny))
        # 사과가 있는지 확인 (in set연산으로 빠르게)
        if (nx, ny) in apples:
            apples.remove((nx, ny))
        else: # 사과가 없으면 꼬리 칸 비워주기
            tx, ty = snake.popleft()
            visited[tx][ty] = False
        # 뱀의 방향 이동 체크
        if time in dir.keys():
            if dir[time] == 'L':
                d = (d-1)%4
            else:
                d = (d+1)%4
        # 좌표 갱신
        x, y = nx, ny
    print(time)
solution()