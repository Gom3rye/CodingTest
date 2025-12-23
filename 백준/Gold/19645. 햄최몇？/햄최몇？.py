import sys
input = sys.stdin.readline

n = int(input())
burgers = list(map(int, input().split()))
total_sum = sum(burgers)

# dp[k][c] = 관우 k, 철환 c 효용 합이 가능한가?
# 1024MB 메모리 제한이 넉넉하므로 O(TotalSum^2) 배열 선언
dp = [[False] * (total_sum + 1) for _ in range(total_sum + 1)]
dp[0][0] = True # 초기값 (0, 0)은 가능

current_total = 0
for b in burgers:
    current_total += b
    # 0/1 냅색: 역방향 순회 (PULL 방식)
    # k + c <= current_total 이므로 c의 범위를 최적화할 수 있음
    for k in range(current_total, -1, -1):
        for c in range(current_total - k, -1, -1):
            
            # 1. b를 G에게 줌 (dp[k][c]는 이전 값을 유지)
            # if dp[k][c]: dp[k][c] = True 
            
            # 2. b를 K에게 줌 (k-b에서 PULL)
            if k >= b and dp[k - b][c]:
                dp[k][c] = True
            
            # 3. b를 C에게 줌 (c-b에서 PULL)
            elif c >= b and dp[k][c - b]:
                dp[k][c] = True

max_g = 0
# 모든 가능한 (k, c) 조합을 확인
for k in range(total_sum + 1):
    for c in range(total_sum - k + 1): # k + c <= total_sum
        
        if dp[k][c]:
            g = total_sum - k - c
            
            # 서열 규칙: K >= C >= G
            if k >= c and c >= g:
                max_g = max(max_g, g)

print(max_g)