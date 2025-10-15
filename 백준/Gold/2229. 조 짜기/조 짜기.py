N = int(input())

score_list = list(map(int, input().split()))
dp = [0]*N
for i in range(N) :
    minval = maxval = score_list[i]
    for j in range(i+1, N) :
        minval = min(minval, score_list[j])
        maxval = max(maxval, score_list[j])
        dpval = dp[i-1] if i > 0 else 0
        dp[j] = max(dp[j], maxval - minval + dpval)

print(dp[-1])