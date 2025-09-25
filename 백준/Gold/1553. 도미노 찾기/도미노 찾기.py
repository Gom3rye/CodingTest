import sys

# 1. 입력 및 상태 변수 초기화
grid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(8)]
# visited[r][c]: (r, c) 칸이 덮였는지 여부
visited = [[False] * 7 for _ in range(8)]
# domino_used[a][b]: (a, b) 도미노를 사용했는지 여부 (a <= b)
domino_used = [[False] * 7 for _ in range(7)]
count = 0

def solve(row, col):
    global count

    # [성공 조건] (8, 0)에 도달하면 모든 칸을 채운 것이므로 경우의 수 1 증가
    if row == 8:
        count += 1
        return

    # 다음 칸 위치 계산
    next_row, next_col = (row, col + 1) if col < 6 else (row + 1, 0)

    # 현재 칸이 이미 덮여있다면, 다음 칸으로 바로 이동
    if visited[row][col]:
        solve(next_row, next_col)
        return

    # --- [탐색] 현재 칸 (row, col)에 도미노 놓기 ---

    # 선택 1: 가로로 놓기
    # [가지치기] 오른쪽 칸이 격자 안에 있고 비어있는지 확인
    if col + 1 < 7 and not visited[row][col + 1]:
        # 도미노 숫자 확인
        d1, d2 = grid[row][col], grid[row][col + 1]
        # 도미노 사용 여부 확인 (작은 수가 앞에 오도록 정렬)
        if d1 > d2: d1, d2 = d2, d1
        
        if not domino_used[d1][d2]:
            # [선택] 상태 변경
            visited[row][col] = visited[row][col + 1] = True
            domino_used[d1][d2] = True
            
            # [다음 단계] 재귀 호출
            solve(next_row, next_col)
            
            # [백트래킹] 상태 원상 복구
            visited[row][col] = visited[row][col + 1] = False
            domino_used[d1][d2] = False

    # 선택 2: 세로로 놓기
    # [가지치기] 아래쪽 칸이 격자 안에 있고 비어있는지 확인
    if row + 1 < 8 and not visited[row + 1][col]:
        # 도미노 숫자 확인
        d1, d2 = grid[row][col], grid[row + 1][col]
        # 도미노 사용 여부 확인
        if d1 > d2: d1, d2 = d2, d1

        if not domino_used[d1][d2]:
            # [선택] 상태 변경
            visited[row][col] = visited[row + 1][col] = True
            domino_used[d1][d2] = True
            
            # [다음 단계] 재귀 호출
            solve(next_row, next_col)
            
            # [백트래킹] 상태 원상 복구
            visited[row][col] = visited[row + 1][col] = False
            domino_used[d1][d2] = False

# (0, 0)부터 탐색 시작
solve(0, 0)
print(count)