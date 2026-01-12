import sys
from math import log2
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, l = map(int, input().split()) # <=100, 경사로의 길이 <=n
    board = [list(map(int, input().split())) for _ in range(n)]
    # 낮은 칸이 l개 연속되어서 놓여야 한다.
    # 경사로가 겹치면 안된다. -> used[T/F] 배열 쓰기
    def is_valid(line):
        used = [False]*n
        for i in range(n-1):
            if line[i] == line[i+1]:
                continue
            if abs(line[i]-line[i+1]) > 1:
                return False
            # 내리막 길인 경우
            if line[i]-1 == line[i+1]:
                for j in range(i+1, i+1+l):
                    # 끝을 넘어가거나 line[i+1]이 l개가 아니거나 이미 경사로가 놓여있다면
                    if j >= n or line[j] != line[i+1] or used[j]:
                        return False
                    # 경사로 놓기
                    used[j] = True
            # 오르막 길인 경우
            if line[i]+1 == line[i+1]:
                for j in range(i-l+1, i+1):
                    if j < 0 or line[j] != line[i] or used[j]:
                        return False
                    used[j] = True
        return True

    cnt = 0
    # 가로 길 탐색 경우
    for i in range(n):
        if is_valid(board[i]):
            cnt += 1

    # 세로 길 탐색 경우
    for j in range(n):
        col = [board[i][j] for i in range(n)]
        if is_valid(col):
            cnt += 1
    print(cnt)
solution()