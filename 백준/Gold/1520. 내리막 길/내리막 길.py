import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def solution():
    # 항상 내리막길로만 이동하는 경로의 개수
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1]*m for _ in range(n)] # dp[i][j]: i,j까지 가는 경우의 수 (미방문 표시를 위해 -1로 초기화)
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def dfs(x, y):
        # 종료 조건: 목적지에 도달하면 1개의 경로를 찾은 것
        if x == n-1 and y == m-1:
            return 1
        
        if dp[x][y] != -1: # memoization (이미 계산된 값 그대로 사용)
            return dp[x][y]
        
        dp[x][y] = 0 # 현재 위치에서 갈 수 있는 경로가 없다고 가정하고 0으로 초기화
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m and board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny)
        # 결과 저장 및 반환
        return dp[x][y]
    print(dfs(0,0))
solution()