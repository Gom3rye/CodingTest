import sys
input = sys.stdin.readline

def solution():
    MOD = 1_000_000
    s = input().strip()
    n = len(s)

    if s[0] == '0':
        print(0)
        return

    dp = [0] * (n + 1)
    dp[0] = 1  # 빈 문자열은 해석 1가지
    dp[1] = 1  # 첫 글자가 0이 아닌 경우

    for i in range(2, n + 1):
        one = int(s[i-1])       # 한 글자
        two = int(s[i-2:i])     # 두 글자

        if 1 <= one <= 9:
            dp[i] += dp[i-1]

        if 10 <= two <= 26:
            dp[i] += dp[i-2]

        dp[i] %= MOD

    print(dp[n])
solution()
