import sys
input = sys.stdin.readline
def solution():
    s = '-1'+input().strip() # 1based index로 만들어주기 위해
    if s[1] == '0': # 암호를 해독할 수 없는 경우
        print(0)
        return
    n = len(s)
    MOD = 1000000
    dp = [0]*n
    dp[1] = 1 # 첫 번째 알파벳 경우는 1
    for i in range(2, n):
        if 1<=int(s[i])<=9:
            dp[i] += dp[i-1]
        if 10<=int(s[i-1:i+1])<=26:
            dp[i] += dp[i-2]
        dp[i] %= MOD
    print(dp[-1])
solution()