import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    # 방향: 0(북), 1(동), 2(남), 3(서)
    directions = {
        0: (-1, 0),  # 북
        1: (0, 1),   # 동
        2: (1, 0),   # 남
        3: (0, -1),  # 서
    }

    cleaned = [[False] * m for _ in range(n)]
    
    while True:
        # 1. 현재 칸 청소
        if not cleaned[x][y]:
            cleaned[x][y] = True

        cleaned_all_adjacent = True

        # 2. 주변 4칸 중 청소 안 된 곳 찾기
        for _ in range(4):
            # 반시계 방향 회전
            d = (d + 3) % 4
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and not cleaned[nx][ny]:
                    # 청소 안 된 칸으로 이동
                    x, y = nx, ny
                    cleaned_all_adjacent = False
                    break  # 청소하러 이동

        if cleaned_all_adjacent:
            # 후진 시도
            back_dir = (d + 2) % 4
            back_dx, back_dy = directions[back_dir]
            bx, by = x + back_dx, y + back_dy

            if 0 <= bx < n and 0 <= by < m and board[bx][by] == 0:
                x, y = bx, by  # 후진
            else:
                break  # 후진 불가 => 작동 멈춤

    # 청소한 칸 수 출력
    count = sum(1 for i in range(n) for j in range(m) if cleaned[i][j])
    print(count)

solution()
