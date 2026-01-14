import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #좌석 <=40
    m = int(input()) # #고정석 <=n
    # 고정된 자리를 잘라서 m+1개의 덩어리로 보자.
    # 규칙 있음! -> dp로 정리
    dp = [1]*(n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    fixed = list(int(input()) for _ in range(m))+[n+1]
    start = 0
    total_cnt = 1
    for fix in fixed:
        cnt = fix-start-1
        start = fix
        total_cnt *= dp[cnt]
    print(total_cnt)
solution()