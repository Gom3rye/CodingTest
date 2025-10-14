N,T = map(int,input().split())
study = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]
dp =[[0]*(T+1) for _ in range(N+1)]

for i in range(1,N+1):
    time = study[i][0]
    score = study[i][1]

    for j in range(1,T+1) :
        if j < time :
            dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        else :
            dp[i][j] = max(score + dp[i-1][j-time], dp[i-1][j])

print(dp[N][T])