import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    # 순증가 최장 길이 구하기 (최장 증가 부분 수열 LIS)
    dp = [1]*n # dp[i]: i까지의 LIS
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))
solution()