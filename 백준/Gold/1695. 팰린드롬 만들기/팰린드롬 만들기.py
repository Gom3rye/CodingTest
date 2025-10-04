n = int(input())
arr = list(map(int, input().split()))
 
# arr i번째까지의 수열과 arr의 역순수열의 j번째까지의 수열의 최장공통부분수열(LCS) 길이 저장
dp = [[0] * (n+1) for _ in range(n+1)]  
 
for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i-1] == arr[n-j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(n-dp[n][n])