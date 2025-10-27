import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_sum = -float('inf') # 최솟값으로 초기화
    for top in range(n):
        cols_sum = [0]*m
        # 아래쪽 행을 하나씩 내려가면서 누적
        for bottom in range(top, n):
            for j in range(m):
                cols_sum[j] += board[bottom][j]
            # kadane's algorithm (1차원 배열에서 연속된 부분 배열의 최대합/최대곱 구하기)
            # dp[i] = max(arr[i], dp[i-1] + arr[i])
            current = 0
            best = -float('inf')
            for val in cols_sum:
                current = max(val, current+val)
                best = max(best, current)
            max_sum = max(max_sum, best)
    print(max_sum)
solution()