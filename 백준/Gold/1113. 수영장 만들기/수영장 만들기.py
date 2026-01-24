import sys, heapq
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    board = [list(map(int, list(input().strip()))) for _ in range(N)]
    
    visited = [[False] * M for _ in range(N)]
    pq = []
    
    # 1. 모든 가장자리 칸을 우선순위 큐에 삽입
    for i in range(N):
        for j in range(M):
            if i == 0 or i == N-1 or j == 0 or j == M-1:
                # (높이, 행, 열) 순서로 삽입
                heapq.heappush(pq, (board[i][j], i, j))
                visited[i][j] = True
                
    total_water = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 2. 가장 낮은 벽부터 꺼내어 인접한 안쪽 칸 탐색
    while pq:
        h, r, c = heapq.heappop(pq)
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                
                # 인접한 안쪽 칸의 높이가 현재 벽(h)보다 낮다면 물이 고임
                if board[nr][nc] < h:
                    total_water += (h - board[nr][nc])
                    # 물이 고인 후의 높이를 새로운 벽의 높이로 간주
                    heapq.heappush(pq, (h, nr, nc))
                else:
                    # 안쪽 칸이 더 높다면 그 칸 자체가 새로운 벽이 됨
                    heapq.heappush(pq, (board[nr][nc], nr, nc))
                    
    print(total_water)
solution()