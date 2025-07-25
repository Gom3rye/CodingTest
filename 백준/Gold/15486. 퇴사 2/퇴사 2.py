import sys
input = sys.stdin.read

def solution():
    data = input().split()
    N = int(data[0])
    dp = [0] * (N + 2)  # N+1일째는 퇴사이므로 N+2 크기로 생성
    max_profit = 0

    idx = 1
    for day in range(1, N + 1):
        Ti = int(data[idx])
        Pi = int(data[idx + 1])
        idx += 2

        # 이전까지의 최대 수익을 현재 위치에 반영
        dp[day] = max(dp[day], max_profit)

        # 상담 가능한 경우
        if day + Ti <= N + 1:
            dp[day + Ti] = max(dp[day + Ti], dp[day] + Pi)

        # 최대 수익 업데이트
        max_profit = max(max_profit, dp[day])

    print(max(dp))

solution()
