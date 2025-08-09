import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 싸움 시간, 시전 시간
    dp = [1] * (n+1) # i초를 만드는 가능한 스킬 조합의 수
    MOD = 1000000007
    for i in range(m, n+1):
        dp[i] = (dp[i-1]+dp[i-m])%MOD
    print(dp[n])
solution()