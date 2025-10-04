import sys
input = sys.stdin.readline
def solution():
    t = int(input()) # 지폐의 금액
    k = int(input()) # 동전의 가지 수
    # 금액, 개수
    coins = [list(map(int, input().split())) for _ in range(k)]
    dp = [0]*(t+1) # dp[i]: i금액을 만드는 경우의 수
    dp[0] = 1 # 0원을 만드는 경우의 수 1
    for coin, cnt in coins:
        for money in range(t, 0, -1): # t원부터 1원까지 내려가며 진행
            for c in range(1, cnt+1): # 현재 동전 coin의 개수만큼 for문 진행
                if money-coin*c >= 0:
                    dp[money] += dp[money-coin*c]
    print(dp[t])
solution()