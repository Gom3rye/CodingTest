import sys

# Python의 재귀 깊이 제한은 기본적으로 1000이므로, N이 커질 경우를 대비해 늘려줍니다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# --- 입력 처리 ---
N = int(input())
jumps = []
# 1번 돌부터 N-1번 돌까지의 점프 정보 입력
for _ in range(N - 1):
    jumps.append(list(map(int, input().split())))
K = int(input())

# --- DP 설정 ---
# dp[돌 번호][매우 큰 점프 사용 여부(0: 미사용, 1: 사용)]
# 매우 큰 값으로 초기화하여 min 연산에 영향을 주지 않도록 함
dp = [[float('inf')] * 2 for _ in range(N)]


def solve(stone_idx, super_jump_used):
    """
    stone_idx번 돌에서, super_jump_used 상태일 때,
    마지막 돌까지 가는 데 필요한 최소 에너지를 반환하는 함수
    """
    # [기저 사례 1] 마지막 돌에 도착한 경우
    if stone_idx == N - 1:
        return 0
    
    # [기저 사례 2] 마지막 돌을 지나친 경우 (잘못된 경로)
    if stone_idx >= N:
        return float('inf')

    # [메모이제이션] 이미 계산한 적 있는 상태라면 저장된 값을 즉시 반환
    if dp[stone_idx][super_jump_used] != float('inf'):
        return dp[stone_idx][super_jump_used]

    # --- 재귀 단계 ---
    
    # 1. 작은 점프 (+1칸)
    # jumps 배열은 0-indexed이므로 stone_idx를 그대로 사용
    res1 = jumps[stone_idx][0] + solve(stone_idx + 1, super_jump_used)

    # 2. 큰 점프 (+2칸)
    res2 = float('inf')
    # 큰 점프를 할 돌이 N-1번째 돌 이내에 있어야 함
    if stone_idx + 2 < N:
        res2 = jumps[stone_idx][1] + solve(stone_idx + 2, super_jump_used)

    # 3. 매우 큰 점프 (+3칸)
    res3 = float('inf')
    # 아직 매우 큰 점프를 사용하지 않았다면 시도 가능
    if not super_jump_used:
        res3 = K + solve(stone_idx + 3, 1) # 사용했으므로 상태를 1로 변경

    # 세 가지 점프 중 최소 비용을 현재 상태의 답으로 저장
    dp[stone_idx][super_jump_used] = min(res1, res2, res3)
    return dp[stone_idx][super_jump_used]

# 0번 돌에서, 매우 큰 점프를 사용하지 않은(0) 상태로 시작
min_energy = solve(0, 0)
print(min_energy)