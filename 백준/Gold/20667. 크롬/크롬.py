import sys

input = sys.stdin.readline
INF = float('inf')

n, m, k = map(int, input().split())
tabs = []
max_p_sum = 0
for _ in range(n):
    c, mem, p = map(int, input().split())
    tabs.append((c, mem, p))
    max_p_sum += p # 가능한 최대 중요도 합

# dp[p][c] = max_memory
# "중요도 합 p, CPU *최소* c를 확보했을 때의 최대 메모리"
# -1은 도달 불가능한 상태를 의미
dp = [[-1] * (m + 1) for _ in range(max_p_sum + 1)]

# 초기값: 중요도 0, CPU 0일 때 메모리 0 확보
dp[0][0] = 0

# 0/1 냅색 (3중 반복문)
for cpu, mem, pri in tabs:
    # 1. 중요도 (역방향)
    for p in range(max_p_sum, pri - 1, -1):
        # 2. CPU (역방향)
        # 0부터 M까지 모든 상태를 확인
        for c in range(m, -1, -1):
            
            # 이전 상태 (p - pri, c)가 도달 가능했다면
            if dp[p - pri][c] != -1:
                
                # "최소 M" 트릭: 
                # c + cpu가 M을 넘어가면 모두 M번 인덱스에 저장
                new_c = min(m, c + cpu)
                
                # 점화식: max(현재 값, 이전 상태에서 탭을 추가한 값)
                dp[p][new_c] = max(dp[p][new_c], dp[p - pri][c] + mem)

# 정답 찾기
min_ans = INF

# 중요도 p를 0부터 순회 (최소 p를 찾아야 하므로)
for p in range(max_p_sum + 1):
    # dp[p][m] : 중요도 p, CPU '최소' m을 만족하는 상태
    if dp[p][m] >= k:
        min_ans = p
        break # 최소 p를 찾았으므로 즉시 종료

if min_ans == INF:
    print(-1)
else:
    print(min_ans)