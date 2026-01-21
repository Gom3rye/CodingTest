import sys
input = sys.stdin.readline
def solution():
    MOD = 1000000
    secret = input().strip() # 5000자리 이하의 암호
    if secret[0] == '0': # 암호가 잘못된 경우
        print(0)
        return
    n = len(secret)
    dp = [0]*(n+1) # dp[i]: i번째 암호를 완성하는 경우
    dp[0] = 1 # 아무 글자도 없는 경우 1 초기화
    dp[1] = 1
    for i in range(2, n+1):
        num1 = int(secret[i-1])
        num2 = int(secret[i-2:i])
        if 1<=num1<10:
            dp[i] += dp[i-1]
        if 10<=num2<27:
            dp[i] += dp[i-2]
        dp[i]%=MOD
    print(dp[-1])
solution()