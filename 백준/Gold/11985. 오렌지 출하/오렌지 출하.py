import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # 오렌지 개수, 최대 개수, 포장 비용
    oranges = [0] * (n + 1) # 1-based 인덱싱을 위해 0번 인덱스 추가
    for i in range(1, n + 1):
        oranges[i] = int(input())
    
    # DP 상태 정의: dp[i] = 1번부터 i번 오렌지까지 포장하는 최소 비용
    INF = float('inf')
    dp = [INF] * (n + 1)
    
    # Base Case: 0개의 오렌지를 포장하는 비용은 0
    dp[0] = 0
    
    # 1번 오렌지부터 n번 오렌지까지 순차적으로 dp 값을 계산
    for i in range(1, n + 1):
        current_max = -1
        current_min = INF
        
        # 마지막 상자의 시작점 'j'를 i부터 거꾸로 탐색
        # (j: i, i-1, i-2, ...)
        for j in range(i, 0, -1):
            
            # 상자에 담긴 오렌지 개수 (j번부터 i번까지)
            s = i - j + 1
            
            # 1. 상자 최대 개수(M) 초과 시 중단
            if s > m:
                break
                
            # 2. 현재 상자(j~i)의 max, min 갱신 (O(1) 최적화)
            # j-1에서 j로 올 때, oranges[j] 값만 새로 고려하면 됨
            current_max = max(current_max, oranges[j])
            current_min = min(current_min, oranges[j])
            
            # 3. 비용 계산
            # Cost(j, i) = K + s * (max(j..i) - min(j..i))
            box_cost = k + s * (current_max - current_min)
            
            # 4. 점화식 적용
            # dp[i] = min(dp[i], (j-1번까지의 최소 비용) + (j~i 상자 비용))
            dp[i] = min(dp[i], dp[j-1] + box_cost)

    # 최종 답: n개의 오렌지를 모두 포장하는 최소 비용
    print(dp[n])
solution()