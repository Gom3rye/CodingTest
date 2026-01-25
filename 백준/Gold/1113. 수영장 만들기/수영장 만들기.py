import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # <=50
    board = [list(map(int, input().strip())) for _ in range(n)]
    # 자신보다 작은 칸을 만나면 총 양에 더하는 방식! (물 빼내며 관리)
    visited = [[False]*m for _ in range(n)]
    q = []
    # 물이 고일 수 없는 모든 가장자리 칸들을 q에 넣고 자신보다 낮은 칸을 만나면 그 기준을 q에 넣으며 탐색
    total = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                heapq.heappush(q, (board[i][j], i, j))
                visited[i][j] = True
    while q:
        h, x, y = heapq.heappop(q)
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True # 방문 처리 해놓고
                if board[nx][ny] < h: # 작으면 물이 고일 수 있음
                    total += (h-board[nx][ny])
                    heapq.heappush(q, (h, nx, ny))
                else: # 같거나 크면 고일 수 없음
                    heapq.heappush(q, (board[nx][ny], nx, ny))
    print(total)
solution()