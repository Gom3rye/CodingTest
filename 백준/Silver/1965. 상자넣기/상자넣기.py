import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    # 증가하는 가장 긴 수열
    arr = list(map(int, input().split()))
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))    
solution()