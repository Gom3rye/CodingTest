import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    l = list(map(int, input().split())) # 체력
    j = list(map(int, input().split())) # 기쁨
    # dp[i]: i만큼 체력을 사용했을 때 얻을 수 있는 최대 기쁨
    dp = [0]*100 # 99까지 체력을 쓸 수 있다.
    for i in range(n):
        cost = l[i]
        joy = j[i]
        for hp in range(99, cost-1, -1): # 맨 뒤에서부터 갱신
            dp[hp] = max(dp[hp], dp[hp-cost]+joy)

    print(max(dp[:100])) # 체력이 0이면 안되니까
solution()