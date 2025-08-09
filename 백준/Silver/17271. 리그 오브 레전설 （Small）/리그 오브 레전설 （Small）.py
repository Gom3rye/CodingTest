import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 싸움 시간, 시전 시간
    dp = [0] * (n+1) # i초를 만드는 가능한 스킬 조합의 수
    dp[0] = 1  # 0초를 만드는 경우의 수는 아무것도 안 하는 1가지
    MOD = 1000000007
    for i in range(1, n+1):
        dp[i] += dp[i-1] # 1초 사용
        if i >= m:
            dp[i] += dp[i-m] # m초 사용
    print(dp[n]%MOD)
solution()