import sys
from collections import deque
input = sys.stdin.readline
def solution():
    board = [list(input().strip()) for _ in range(12)]
    # 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다 -> 탐색/삭제 로직 []로 담아놨다가 분리하기
    # 한 그룹인지 파악하는 함수
    def is_group(x, y):
        color = board[x][y]
        visited[x][y] = True
        group = [(x, y)]
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    group.append((nx, ny))
                    q.append((nx, ny))
        return group
    
    def gravity():
        # 열 별로 아래 행부터 검사
        for col in range(6):
            fall = deque()
            for row in range(11, -1, -1):
                if board[row][col] != '.':
                    fall.append(board[row][col]) # 색깔들만 모아서
            # 재배치
            for row in range(11, -1, -1):
                if fall:
                    board[row][col] = fall.popleft() # 왼쪽에서 꺼냄!
                else:
                    board[row][col] = '.'
                    
    time = 0
    while True: # 한 사이클: 보드 한 번 훑어서 연쇄작용 몇 번 있는지 파악하기
        visited = [[False]*6 for _ in range(12)] # 한 사이클이 끝나면 새 보드가 탄생하니까 이에 맞춰 방문처리 초기화
        disappear = []
        for i in range(12):
            for j in range(6):
                if board[i][j] != '.' and not visited[i][j]:
                    group = is_group(i, j)
                    if len(group) >= 4:
                        disappear.extend(group)
        if disappear:
            time += 1 # 연쇄 작용 1번 추가
            for x, y in disappear:
                board[x][y] = '.' # 터짐
                # 내려가기 로직
            gravity()
        else:
            break
    print(time)
solution()