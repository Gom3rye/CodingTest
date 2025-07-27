import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    # 3번째 숫자까지 와도 결과값이 다를 수 있다. -> 각 숫자마다 어떤 값이 되는지 상태 추적 필요
    dp = [[0]*21 for _ in range(n-1)] # dp[i][j]: i번째 숫자까지의 계산해서 현재 결과가 j가 되는 경우의 수
    dp[0][arr[0]] = 1 # 첫 번째 숫자의 결과는 하나
    for i in range(1, n-1):
        for j in range(21):
            if dp[i-1][j]: # i번째 숫자 전에 j라는 값이 0이 아니라면
                if j+arr[i] <= 20:
                    dp[i][j+arr[i]] += dp[i-1][j]
                if j-arr[i] >= 0:
                    dp[i][j-arr[i]] += dp[i-1][j]
    print(dp[n-2][arr[-1]]) # n-2번째 숫자까지의 결과가 arr의 마지막 원소일 경우의 수
solution()