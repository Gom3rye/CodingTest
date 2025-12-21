import sys
from collections import deque
input = sys.stdin.readline
def solution():
    t = int(input()) # <=100
    for _ in range(t):
        h, w = map(int, input().split()) # <=100
        board = ['.'*(w+2)]
        for _ in range(h):
            board.append('.'+input().strip()+'.')
        board.append('.'*(w+2))
        # padding값 계산해서 resize
        h += 2
        w += 2
        keys = input().strip() # 상근이가 가지고 있는 열쇠, 없으면 '0'
        if keys != '0':
            keys = set(keys)
        else:
            keys = set()
        door_candidates = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key_candidates = door_candidates.lower()
        
        # 문을 발견했을 때 좌표값을 저장할 보류 리스트 (열쇠를 발견했을 때 바로 이 문 위치로 jump하기 위함)
        doors_on_hold = {char: [] for char in door_candidates} #or {chr(i): [] for i in range(ord('A'), ord('Z')+1)}
        q = deque([(0, 0)]) # 확실한 .값에서 시작
        visited = [[False]*w for _ in range(h)]
        visited[0][0] = True
        answer = 0
        while q:
            x, y = q.popleft()
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = dx+x, dy+y
                if not (0<=nx<h and 0<=ny<w):
                    continue
                if board[nx][ny] == '*':
                    continue
                if visited[nx][ny]:
                    continue

                now = board[nx][ny]
                # 열쇠인 경우
                if now in key_candidates: # ord('a') <= ord(board[nx][ny]) <= ord('z'):
                    keys.add(now)
                    door = now.upper()
                    # 해당 열쇠로 열 수 있는 문이 보류 후보에 있는 경우
                    if door in doors_on_hold:
                        for doorx, doory in doors_on_hold[door]:
                            visited[doorx][doory] = True
                            q.append((doorx, doory))

                # 문인 경우
                if now in door_candidates:
                    # 열쇠가 있는 경우 방문 가능
                    if now.lower() in keys:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    else: # 열쇠가 없는 경우 보류 후보에 저장
                        doors_on_hold[now].append((nx, ny))
                    continue

                # $인 경우
                if now == '$':
                    answer += 1

                # ./열쇠인 경우
                visited[nx][ny] = True
                q.append((nx, ny))
        print(answer)
solution()