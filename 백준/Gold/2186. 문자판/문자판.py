import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # k개의 칸만큼 이동할 수 있다.
    board = [input().strip() for _ in range(n)]
    word = input().strip()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    if k != 1:
        tmpk = 2
        temp = []
        while tmpk <= k:
            for dx, dy in directions:
                nx, ny = dx*tmpk, dy*tmpk
                temp.append((nx, ny))
            tmpk += 1
        directions.extend(temp)

    wlen = len(word)
    dp = [[[-1]*wlen for _ in range(m)] for _ in range(n)]
    def dfs(x, y, idx):
        # 단어의 마지막 글자까지 완성한 겨우
        if idx == wlen-1:
            return 1
        # 메모이제이션
        if dp[x][y][idx] != -1:
            return dp[x][y][idx]
        cnt = 0
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == word[idx+1]:
                cnt += dfs(nx, ny, idx+1)
        # 계산된 결과를 dp 테이블에 저장
        dp[x][y][idx] = cnt
        return cnt

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                answer += dfs(i, j, 0)
    print(answer)
solution()