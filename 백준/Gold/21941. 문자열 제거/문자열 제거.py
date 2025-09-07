import sys
input = sys.stdin.readline
def solution():
    s = input().strip()
    m = int(input()) # 지울 수 있는 문자열 개수 m
    strings = {}
    for _ in range(m):
        a, x = input().split()
        # 길이보단 큰 값일 때만 저장
        if len(a) < int(x):
            strings[a] = int(x) # 점수 저장

    n = len(s)
    dp = [0]*(n+1) # dp[i]: i를 지웠을 때 얻을 수 있는 가장 큰 점수

    for i in range(1, n+1):
        dp[i] = dp[i-1]+1
        for a, x in strings.items():
            lena = len(a)
            if i-lena >= 0 and s[i-lena:i] == a:
                dp[i] = max(dp[i], dp[i-lena]+x)

    print(dp[-1])
solution()