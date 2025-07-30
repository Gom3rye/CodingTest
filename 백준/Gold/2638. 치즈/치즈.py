import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    direction = [(1,0), (0,1), (-1,0), (0,-1)]
    # 공기에 따라고 외부 공기, 내부 공기로 나눠지고 그에 따라 처리를 다르게 해줘야 하므로 중요한 것은 치즈가 아닌 공기!
    air = deque([(0,0)]) # 모는 종이의 맨 가장자리에는 치즈가 높이지 않는 것으로 가정하니까
    hour = 0
    cheese[0][0] = -1 # -1: 확인 한 외부 공기, 0: 공기, 1: 치즈
    while air: # 외부 BFS: 시뮬레이션 시간 흐름을 제어한다.(1시간 단위 시뮬레이션 반복)
        next_air = deque() # 치즈가 녹아서 공기가 될 좌표들 모은 덱
        while air: # 내부 BFS: 1시간 동안 외부공기 BFS로 전파시키기
            x, y = air.popleft()
            for dx, dy in direction:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<m:
                    if cheese[nx][ny] == -1:
                        continue # 확인한 외부 공기는 패쓰
                    
                    elif cheese[nx][ny] == 0:
                        air.append((nx, ny))
                        cheese[nx][ny] = -1
                    
                    elif cheese[nx][ny] == 1: # 치즈일 때 air나 next_air로 append 없음 -> 내부 공기 접근 불가
                        cheese[nx][ny] += 1
                    
                    else:
                        next_air.append((nx,ny))
                        cheese[nx][ny] = -1 # 2면 이상 만났다는 뜻이므로 다음 턴에 사라질 외부 공기로 추가
        air = next_air
        hour += 1 # 반복문 끝에 있어서 종료 직전에도 증가되어서 값이 1 커진다.

    print(hour-1) # air가 비어서 종료 시점에 만난 것 빼주기

solution()