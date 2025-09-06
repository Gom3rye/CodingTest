import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 대포알 수
    tetrahedrons = [0]*(n+1)
    for i in range(1, n+1):
        tetrahedrons[i] = i*(i+1)*(i+2)//6
    dp = [float('inf')]*(n+1) # dp[i]: i개의 대포알로 만들 수 있는 사면체의 최소 개수
    dp[0] = 0
    for tet in tetrahedrons[1:]:
        for i in range(tet, n+1):
            dp[i] = min(dp[i], dp[i-tet]+1)
    print(dp[n])
solution()