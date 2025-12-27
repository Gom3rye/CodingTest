import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 거스름돈 액수<=100,000
    dp = [float('inf')]*(n+1)
    dp[0] = 0 # 0원을 거슬러 주는 경우는 0로 초기화
    for num in range(1, n+1):
        if num >= 2:
            dp[num] = min(dp[num], dp[num-2]+1)
        if num >= 5:
            dp[num] = min(dp[num], dp[num-5]+1)
    print(dp[-1] if dp[-1] != float('inf') else -1)
solution()