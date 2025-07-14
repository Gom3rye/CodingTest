from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 핵심! 복잡한 바깥 테두리를 잘 따라갈 수 있도록 좌표들을 모두 2배로 키우기
    # 테두리는 1로, 이미 지나온 테두리는 -1로, 기본 초기화 상태는 0으로
    board = [[0]*102 for _ in range(102)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: 2*x, rec)
        # 직사각형의 내부를 2으로 채운다.
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                # 테두리가 아닌 내부 공간은 2로 표시
                if y1<y<y2 and x1<x<x2:
                    board[y][x] = 2 # 내부 공간
                elif board[y][x] != 2:
                    board[y][x] = 1 # 테두리
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    def bfs(sx, sy, ex, ey): # 시작 좌표와 도착 좌표
        q = deque([(sx, sy, 0)]) # 시작, 거리
        board[sy][sx] = -1 # 시작점 방문 처리
        
        while q:
            x, y, dist = q.popleft()
            if x == ex and y == ey:
                return dist//2 # 모두 2배 해줬으니 결과는 반으로 나누기
            
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                # 맵 범위 안이고 테두리인 경우
                if 0<=nx<102 and 0<=ny<102 and board[ny][nx] == 1:
                    q.append((nx, ny, dist+1))
                    board[ny][nx] = -1 # 방문 처리
    answer = bfs(2*characterX, 2*characterY, 2*itemX, 2*itemY)
                    
    return answer