import sys
input = sys.stdin.readline
def solution():
    # 항상 내리막길로만 이동하는 경로의 개수
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)] # dp[i][j]: i,j까지 갈 수 있는 경우의 수
    # dp 초기화
    dp[0][0] = 1
    # 높>낮 으로 진행 -> 낮은 수의 칸을 가는 경우의 수를 구하기 위해선 높은 수의 칸을 가는 경우의 수가 이미 정해져야 한다.
    # 높은 수대로 정렬 => 그 순서로 돌리자.
    settings = []
    for i in range(n):
        for j in range(m):
            settings.append((board[i][j], i,j))
    settings.sort(reverse=True)

    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    for _, x, y in settings:
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m and board[nx][ny] < board[x][y]:
                dp[nx][ny] += dp[x][y]
    print(dp[n-1][m-1])
solution()