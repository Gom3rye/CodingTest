import sys
from collections import deque
input = sys.stdin.readline
def rotate(spots):
    result = []
    for r, c in spots:
        result.append((c, -r)) # cw로 90도 회전: (r,c) => (c,-r)
    min_r, min_c = min(r for r, _ in result), min(c for _, c in result)
    # 0,0으로 모는 정규화 (0,0을 기준으로 정렬되어 있음)
    return sorted((r-min_r, c-min_c) for r, c in result)

def bfs(board, n, x, y, target):
    result = [(x,y)] # 빈칸/좌표만 모아서 정규화 후 반환
    q = deque([(x, y)])
    board[x][y] = 1-target # 방문 처리 (1->0, 0->1)
    while q:
        x, y = q.popleft()
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == target:
                board[nx][ny] = 1-target # 방문 처리
                result.append((nx, ny))
                q.append((nx, ny))
    
    # 정규화 해서 리턴!
    min_x, min_y = min(x for x, _ in result), min(y for _, y in result)
    return sorted((x-min_x, y-min_y) for x, y in result)
                
def solution(game_board, table):
    n = len(table)
    # 게임보드의 빈칸 좌표들 수집
    spaces = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                spaces.append(bfs(game_board, n, i, j, 0))
                
    # table의 실제 좌표 수집
    puzzles = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                puzzles.append(bfs(table, n, i, j, 1))
    
    # 실제 모든 puzzle을 space와 비교해보며 완탐!
    answer = 0 # 최대한 채워넣은 칸 수
    used = [False]*len(puzzles)
    for space in spaces:
        for i in range(len(puzzles)):
            puzzle = puzzles[i]
            # 이미 쓴 퍼즐이거나 칸 수가 다르다면 볼 것도 없음
            if used[i] or len(space) != len(puzzle):
                continue
            # 4번 회전해보며 딱 맞는지 탐색
            temp = puzzle
            found = False
            for dir in range(4):
                if temp == space:
                    answer += len(puzzle)
                    found = True
                    used[i] = True
                    break
                temp = rotate(temp)
            if found:
                break
    return answer