import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    # 모든 오렌지를 포장하는 비용의 최솟값을 구하기
    n, m, k = map(int, input().split()) # 오렌지 개수, 한 상자에 넣을 수 있는 최대 오렌지, 상자 포장 비용
    oranges = [0]+[int(input()) for _ in range(n)] # 1based index
    # dp 상태 정의: dp[orange]: i개의 오렌지를 포장한 최소 비용
    INF = float('inf')
    dp = [INF]*(n+1)
    dp[0] = 0
    # 비용: k+cnt*(max-min)
    # 점화식: dp[i+j] = min(dp[i+j], dp[i]+k+j*(max-min)
    for i in range(n+1):
        # i번까지 포장하는게 불가능하다면(도달할 수 없는 상태)
        if dp[i] == INF:
            continue
        min_orange = INF
        max_orange = -1
        # j: 상자의 사이즈
        for j in range(1, m+1): # m개까지 한 상자에 넣을 수 있다.
            end = i+j # 새 상자의 끝 인덱스
            if end < n+1: # 범위 안에 있다면
                min_orange = min(min_orange, oranges[end])
                max_orange = max(max_orange, oranges[end])
                cost = k+j*(max_orange-min_orange)
                dp[end] = min(dp[end], dp[i]+cost)
    print(dp[-1])
solution()