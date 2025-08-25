import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solution():
    t = int(input())
    for _ in range(t):
        board = [list(map(int, input().split())) for _ in range(11)]
        max_score = 0
        position = [False]*11
        def backtracking(n, score):
            nonlocal max_score
            if n == 11:
                max_score = max(max_score, score)
                return
            for i in range(11):
                if not position[i] and board[n][i] != 0:
                    position[i] = True
                    backtracking(n+1, score+board[n][i])
                    position[i] = False
        backtracking(0, 0)
        print(max_score)
solution()