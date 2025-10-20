import sys
input=sys.stdin.readline

n,m=map(int,input().split()) #n<=100
no=list(map(int,input().split()))
inf=sys.maxsize

dp=[[inf]*106 for _ in range(106)]
dp[0][0]=0

for i in range(n+1):
    for j in range(40): ##최대 쿠폰 발행 갯수 ==40개
        if dp[i][j]==inf:
            continue
        result=dp[i][j]
        if i+1 in no:
            dp[i+1][j]=min(result,dp[i+1][j])
        if j>=3:
            dp[i+1][j-3]=min(result,dp[i+1][j-3])
            
        #1일권
        dp[i+1][j]=min(dp[i+1][j],result+10000)
        #3일권
        for k in range(1,4):
            dp[i+k][j+1]=min(dp[i+k][j+1],result+25000)
        #5일권
        k=0
        for k in range(1,6):
            dp[i+k][j+2]=min(dp[i+k][j+2],result+37000)
print(min(dp[n]))