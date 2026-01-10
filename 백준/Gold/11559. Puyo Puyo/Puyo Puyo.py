import sys
from collections import deque
input = sys.stdin.readline
def solution():
    board = [list(input().strip()) for _ in range(12)]
    # 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.
    # 좌표들을 다 저장해서 구현해야 생각했는데 이는 더 복잡하고 그냥 열별로 아래부터 보면서 위로 올라가면 gravity 함수를 보다 쉽게 작성할 수 있다.
    def gravity(): # 연쇄작용이 있을때 호출하는 함수
        for col in range(6):
            for row in range(11, -1, -1):
                if board[row][col] != '.':
                    color = board[row][col]
                    board[row][col] = '.' # 추락 표시
                    r = row
                    while r+1 < 12 and board[r+1][col] == '.':
                        r += 1 # 내려가기
                    board[r][col] = color # 추락 완료
    
    def is_group(x, y):
        q = deque([(x, y)])
        visited[x][y] = True
        color = board[x][y]
        disappear = [(x, y)] # 사라질 예정인 것들
        while q:
            x, y = q.popleft()
            for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny]:
                    if board[nx][ny] == color:
                        visited[nx][ny] = True
                        disappear.append((nx, ny))
                        q.append((nx, ny))
        if len(disappear) >= 4:
            return disappear
        return None
        
    answer = 0 # 총 연쇄 횟수
    while True: # 연쇄반응이 없을때까지 반복
        total_disappear = []
        visited = [[False]*6 for _ in range(12)]
        for i in range(12):
            for j in range(6):
                if board[i][j] != '.':
                    disappear = is_group(i, j)
                    if disappear == None:
                        continue
                    total_disappear.extend(disappear)
        if total_disappear:
            answer += 1
            for x, y in total_disappear:
                board[x][y] = '.'
            gravity()
        else:
            break
    print(answer)
solution()