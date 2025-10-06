import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    sizes = []
    r, c = map(int, input().split())
    sizes.append(r)
    sizes.append(c)
    for _ in range(n-1):
        _, c = map(int, input().split())
        sizes.append(c)
    dp = [[0]*n for _ in range(n)] # dp[i][j]: i번째 행렬부터 j번째 행렬까지 곱하는 데 필요한 최소 곱셈 연산 횟수
    # cnt: 곱하는 행렬의 개수 (구간의 길이)
    for cnt in range(2, n+1):
        for i in range(n-cnt+1):
            j = i+cnt-1
            dp[i][j] = float('inf') # 초기값으로 매우 큰 수 지정
            for k in range(i, j):
                cost = dp[i][k]+dp[k+1][j]+sizes[i]*sizes[k+1]*sizes[j+1]
                dp[i][j] = min(dp[i][j], cost)
    print(dp[0][n-1]) # 0~n-1번째 행렬까지 곱하는 최소 비용
solution()