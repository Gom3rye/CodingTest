import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 대포알 수
    triangles = [0]*(n+1)
    for i in range(1, n+1):
        triangles[i] = triangles[i-1]+i
    tetrahedrons = [0]*(n+1)
    for i in range(1, n+1):
        tetrahedrons[i] = tetrahedrons[i-1] + triangles[i]
    dp = [float('inf')]*(n+1) # dp[i]: i개의 대포알로 만들 수 있는 사면체의 최소 개수
    dp[0] = 0
    for tet in tetrahedrons[1:]:
        for i in range(tet, n+1):
            dp[i] = min(dp[i], dp[i-tet]+1)
    print(dp[n])
solution()