import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    visited = [[-1]*m for _ in range(n)] # -1: 미방문, 1: 방문 중, 2: 방문 완료
    # dfs + dp memoization
    dp = [[0]*m for _ in range(n)] # dp[x][y]: (x,y)에서 시작했을 때 움직일 수 있는 최대 횟수
    def dfs(x, y):
        if dp[x][y] != 0:
            return dp[x][y]
        
        max_count = 0
        if visited[x][y] == -1:
            visited[x][y] = 1
            k = int(board[x][y])
            for dx, dy in directions:
                nx, ny = x+dx*k, y+dy*k
                if 0<=nx<n and 0<=ny<m and board[nx][ny] != 'H':
                    max_count = max(max_count, dfs(nx, ny)+1)

        elif visited[x][y] == 1:
            # 사이클을 만났다는 뜻이므로
            print(-1)
            sys.exit()

        visited[x][y] = 2
        dp[x][y] = max_count
        return dp[x][y]

    print(dfs(0,0)+1) # 밖으로 나가는 것도 포함시켜야 하니까
solution()