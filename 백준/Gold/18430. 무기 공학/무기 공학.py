import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_score = 0
    visited = [[False]*m for _ in range(n)]

    def backtracking(idx, score):
        nonlocal max_score
        if idx == n*m:
            max_score = max(max_score, score)
            return
        # 2중 for문으로 만들면 검사 완료한 곳도 다시 봐야 하니까 2차원배열 flatten 해서 idx로 검사
        x, y = idx//m, idx%m

        # 현재 칸에 놓는 경우
        if not visited[x][y]:
            # ┏ 모양 (0,0)이 중심
            if x+1<n and y+1<m and not visited[x][y+1] and not visited[x+1][y]:
                visited[x][y] = visited[x][y+1] = visited[x+1][y] = True
                backtracking(idx+1, score+board[x][y]*2+board[x][y+1]+board[x+1][y])
                visited[x][y] = visited[x][y+1] = visited[x+1][y] = False
            # ㄱ 모양
            if x+1<n and 0<=y-1 and not visited[x][y-1] and not visited[x+1][y]:
                visited[x][y] = visited[x][y-1] = visited[x+1][y] = True
                backtracking(idx+1, score+board[x][y]*2+board[x][y-1]+board[x+1][y])
                visited[x][y] = visited[x][y-1] = visited[x+1][y] = False
            # ┛ 모양
            if 0<=x-1 and 0<=y-1 and not visited[x][y-1] and not visited[x-1][y]:
                visited[x][y] = visited[x][y-1] = visited[x-1][y] = True
                backtracking(idx+1, score+board[x][y]*2+board[x][y-1]+board[x-1][y])
                visited[x][y] = visited[x][y-1] = visited[x-1][y] = False
            # ㄴ 모양
            if 0<=x-1 and y+1<m and not visited[x][y+1] and not visited[x-1][y]:
                visited[x][y] = visited[x][y+1] = visited[x-1][y] = True
                backtracking(idx+1, score+board[x][y]*2+board[x][y+1]+board[x-1][y])
                visited[x][y] = visited[x][y+1] = visited[x-1][y] = False
        
        # 현재 칸 놓지 않는 경우도 고려
        backtracking(idx+1, score)

    backtracking(0, 0)
    print(max_score)
solution()