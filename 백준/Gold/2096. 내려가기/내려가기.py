import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    first = list(map(int, input().split()))

    # 초기 상태 설정
    max_dp = first[:]
    min_dp = first[:]

    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        
        # 임시 값 저장 (이전 값 기준으로 계산)
        max0 = max(max_dp[0], max_dp[1]) + a
        max1 = max(max_dp[0], max_dp[1], max_dp[2]) + b
        max2 = max(max_dp[1], max_dp[2]) + c

        min0 = min(min_dp[0], min_dp[1]) + a
        min1 = min(min_dp[0], min_dp[1], min_dp[2]) + b
        min2 = min(min_dp[1], min_dp[2]) + c

        # dp 갱신
        max_dp = [max0, max1, max2]
        min_dp = [min0, min1, min2]

    # 결과 출력
    print(max(max_dp), min(min_dp))
solution()