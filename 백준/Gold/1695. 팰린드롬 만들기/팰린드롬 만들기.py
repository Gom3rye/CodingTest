import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    rra = arr[::-1]
    # 팰린드롬 만들기위해 필요한 최소 개수 = len(arr)-LCS
    # LCS 계산을 위한 DP 테이블 초기화 (크기는 (n+1)x(n+1))
    dp = [[0]*(n+1) for _ in range(n+1)] # dp[i][j]: arr의 i번째까지와 rra의 j번째까지의 LCS 길이
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 원본 수열의 i번째 문자와 뒤집은 수열의 j번째 문자가 같다면
            if arr[i-1] == rra[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(n-dp[-1][-1])
solution()