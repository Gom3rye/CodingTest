import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 수열의 크기
    arr = list(map(int, input().split()))
    m = int(input()) # 질문의 개수
    # 그냥 하면 n<=2000, m<=1,000,000 이므로 시간초과
    dp = [[False]*n for _ in range(n)] # dp[i][j]: i~j까지 팰린드롬 여부
    # 1자리수면 True
    for i in range(n):
        dp[i][i] = True
    # 2자리수면
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            dp[i][i+1] = True
    # 3자리수 이상
    for i in range(n-3, -1, -1):
        for j in range(i+2, n):
            if arr[i] == arr[j] and dp[i+1][j-1]:
                dp[i][j] = True
    result = []
    for _ in range(m):
        start, end = map(int, input().split())
        if dp[start-1][end-1]:
            result.append(1)
        else:
            result.append(0)
    print("\n".join(map(str, result)))
solution()