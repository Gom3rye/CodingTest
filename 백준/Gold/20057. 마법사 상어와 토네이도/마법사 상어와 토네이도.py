import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    # 왼쪽 방향 모래 확산 패턴
    spread = [
        (-1,0,0.07), # (x, y, percentage)
        (-1,-1,0.1),
        (-1,1,0.01),
        (-2,0,0.02),
        (0,-2,0.05),
        (1,-1,0.1),
        (1,0,0.07),
        (1,1,0.01),
        (2,0,0.02),
        (0,-1,0) # 알파 자리
    ]
    # 좌표 회전 함수 (r, c) -> (-c, r) (90도 반시계 회전)
    def rotate(pattern):
        new_pattern = []
        for r, c, p in pattern:
            new_pattern.append((-c, r, p))
        return new_pattern
    sx, sy = n//2, n//2 # 첫 시작은 격자의 가운데부터
    d = 0 # 첫 방향은 왼쪽부터
    dist = 1 # 첫 거리는 1부터
    outside_sand = 0 # 밖으로 나간 모래 양 구하기

    while True:
        for _ in range(2): # 거리는 2번이 지나고 나면 +1씩 증가
            dx, dy = directions[d]
            for _ in range(dist): ## 토네이도는 한 번에 한 칸 이동하는 점 주의!!
                nx, ny = dx+sx, dy+sy
                if ny < 0: # 토네이도 소멸 조건
                    print(outside_sand)
                    return

                sand = board[nx][ny] # y의 모래양
                # 모래 뿌리기
                board[nx][ny] = 0
                temp_sand = 0 # 알파를 구하기 위한 변수
                for r, c, p in spread:
                    snx, sny = nx+r, ny+c # sand_nx, sand_sy

                    if 0<=snx<n and 0<=sny<n: # 범위 안이면
                        if p == 0: # 알파인 경우
                            board[snx][sny] += sand-temp_sand
                        else:
                            board[snx][sny] += int(sand*p)
                            temp_sand += int(sand*p)
                    else:
                        if p == 0: # 알파인 경우
                            outside_sand += sand-temp_sand
                        else:
                            outside_sand += int(sand*p)
                            temp_sand += int(sand*p)
                # 초기 위치 바꾸기
                sx, sy = nx, ny
            # 방향 바꾸고 spread 회전시키기
            d = (d+1)%4
            spread = rotate(spread)
        dist += 1
solution()