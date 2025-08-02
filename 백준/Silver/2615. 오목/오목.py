import sys
input = sys.stdin.readline

def check_win():
    # 19x19 바둑판 정보 입력
    board = [list(map(int, input().split())) for _ in range(19)]

    # 4가지 방향 벡터: 가로, 세로, 우하향 대각선, 우상향 대각선
    # (dr, dc) -> (row, column) change
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    # 바둑판의 모든 칸을 순회
    for r in range(19):
        for c in range(19):
            if board[r][c] != 0:
                stone_color = board[r][c]

                # 4가지 방향에 대해 오목 여부 확인
                for dr, dc in directions:
                    count = 1
                    
                    # 1. 육목 방지: 시작점의 반대 방향에 같은 돌이 있는지 확인
                    # (r, c)가 오목의 진짜 시작점인지 확인하는 과정
                    prev_r, prev_c = r - dr, c - dc
                    if 0 <= prev_r < 19 and 0 <= prev_c < 19 and board[prev_r][prev_c] == stone_color:
                        continue # 이 방향으로는 이미 확인되었거나, 육목의 일부임

                    # 2. 오목 확인: (r, c)부터 한 방향으로 연속된 돌 개수 세기
                    next_r, next_c = r + dr, c + dc
                    while 0 <= next_r < 19 and 0 <= next_c < 19 and board[next_r][next_c] == stone_color:
                        count += 1
                        next_r += dr
                        next_c += dc
                    
                    # 3. 승리 판정
                    if count == 5:
                        print(stone_color)
                        # 출력 좌표는 1-based index
                        print(r + 1, c + 1)
                        return

    # 승부가 결정되지 않은 경우
    print(0)

check_win()