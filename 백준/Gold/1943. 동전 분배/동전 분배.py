import sys

# sys.stdin.readline을 사용해야 시간 초과가 나지 않습니다.
input = sys.stdin.readline

def solve():
    n = int(input())
    coins = []
    total_sum = 0
    for _ in range(n):
        v, c = map(int, input().split())
        coins.append((v, c))
        total_sum += v * c

    # 1. 총합이 홀수면 바로 0 리턴
    if total_sum % 2 != 0:
        return 0

    target_sum = total_sum // 2

    # 2. DP 배열 선언
    # dp[k] = 금액 k를 만들 수 있는가?
    dp = [False] * (target_sum + 1)
    dp[0] = True # 0원은 항상 만들 수 있음

    # 3. DP 진행 (O(N * Target) 최적화)
    for v, c in coins:
        # count[k] = 금액 k를 만들기 위해 
        # *이번 동전(v)*을 몇 개 사용했는가?
        # ★★★ 동전 종류가 바뀔 때마다 count 배열은 초기화되어야 함
        count = [0] * (target_sum + 1)

        # ★★★ 정방향(v -> target_sum) 순회
        for k in range(v, target_sum + 1):
            
            # 1. (기준점) v 동전 없이 k를 이미 만들 수 있었다면
            if dp[k]:
                count[k] = 0 # v 동전 0개 사용으로 기록
            
            # 2. (점화식) k는 못 만들지만 (k-v)는 만들 수 있었고, 
            #    v 동전 사용 횟수가 c개 미만이라면
            elif dp[k - v] and count[k - v] < c:
                dp[k] = True # k를 만들 수 있게 됨
                count[k] = count[k - v] + 1 # v 동전 1개 더 썼다고 기록
    
    # 4. 최종 결과 반환
    return 1 if dp[target_sum] else 0

# 문제에서 총 3개의 입력을 처리하라고 했습니다.
for _ in range(3):
    print(solve())