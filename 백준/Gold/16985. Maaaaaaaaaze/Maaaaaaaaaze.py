import sys
from collections import deque
from itertools import permutations, product
input = sys.stdin.readline
INF = float('inf')
def solution():
    def rotate(b):
        # 시계방향으로 회전한 보드 반환 (뒤집고 전치)
        return [list(row) for row in zip(*b[::-1])]
    # 120(5!, 순서)*1024(4**5, 회전)*125(3차원) = 약 1500만번의 연산 필요 -> 크니까 미리 가능한 보드의 모습들을 모두 미리 계산해놓자!
    board = [] # 4차원
    for _ in range(5):
        # layer(한 판) 3차원
        layer = [[list(map(int, input().split())) for _ in range(5)]]
        # 가능한 회전 경우를 다 더하기
        for _ in range(3):
            layer.append(rotate(layer[-1]))
        board.append(layer)
    
    directions = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    min_dist = INF
    def bfs(cube):
        visited = [[[False]*5 for _ in range(5)] for _ in range(5)]
        visited[0][0][0] = True
        q = deque([(0,0,0,0)]) # z, x, y, dist
        while q:
            z, x, y, dist = q.popleft()
            # 가지치기
            if dist >= min_dist:
                continue
            if z == x == y == 4:
                return dist
            
            for dz, dx, dy in directions:
                nz, nx, ny = dz+z, dx+x, dy+y
                if 0<=nz<5 and 0<=nx<5 and 0<=ny<5 and not visited[nz][nx][ny] and cube[nz][nx][ny] == 1:
                    visited[nz][nx][ny] = True
                    q.append((nz, nx, ny, dist+1))
            
        return INF # 시작점~도착점까지 도달하지 못하는 경우
    
    # 모든 경우의 수를 순열과 중복 조합을 이용해 계산!
    for order in permutations(range(5)): # 5개의 층 순서대로 쌓기
        for rot in product(range(4), repeat=5): # 4개의 회전 버전 중복 조합으로 5번 고르기
            # cube: board[layer][rotation] 구조
            cube = [board[order[i]][rot[i]] for i in range(5)]
            # 시작점과 도착점은 반드시 도달 가능한 1이어야 한다.
            if cube[0][0][0] == 0 or cube[4][4][4] == 0:
                continue
            dist = bfs(cube)
            min_dist = min(min_dist, dist)
            if min_dist == 12: # 논리상의 최적의 답이니 다른 경우 볼 필요 없이 바로 출력
                print(12)
                return
    
    print(min_dist if min_dist != INF else -1)

solution()