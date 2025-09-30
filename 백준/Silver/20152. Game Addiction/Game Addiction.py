import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def solution():
    h, n = map(int, input().split()) # 집 좌표(h,h), pc방 좌표(n,n)
    directions = [(0,1),(1,0)]
    l = abs(h-n) # len
    dp = [[-1]*(l+1) for _ in range(l+1)] # dp[i][j]: (i,j)를 갈 수 있는 경로의 수
    # (0, 0)~(l, l)까지 갈 수 있는 최단 경로의 수 구하기
    def dfs(x, y):
        # 위 삼각형은 침수 지역
        if y > x:
            return 0
        if x == l and y == l:
            return 1
        if dp[x][y] != -1:
            return dp[x][y]
        
        cnt = 0
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<=l and 0<=ny<=l:
                cnt += dfs(nx, ny)

        dp[x][y] = cnt
        return cnt
    print(dfs(0, 0))
solution()