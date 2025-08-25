import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solution():
    t = int(input())
    for _ in range(t):
        board = [list(map(int, input().split())) for _ in range(11)]
        max_score = 0
        position = set()
        def backtracking(n, score):
            nonlocal max_score
            if n == 11:
                max_score = max(max_score, score)
                return
            for i in range(11):
                if i not in position and board[n][i] != 0:
                    position.add(i)
                    backtracking(n+1, score+board[n][i])
                    position.remove(i)
        backtracking(0, 0)
        print(max_score)
solution()