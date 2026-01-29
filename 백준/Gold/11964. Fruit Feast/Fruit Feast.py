import sys
input = sys.stdin.readline
def solution():
    t, a, b = map(int, input().split()) # maximum fullness <=5,000,000, orange increase, lemon increase <=t
    # 물 최대 1번 마실 수 있고 물 마시면 포만감 //2 됨
    # 무제한 냅색! -> 물 마신경우 / 안 마신경우 각각 나올 수 있는 포만감 다르니까 둘 다 구분해서 탐색
    no_water_dp = [False]*(t+1) # if dp[i]: i의 포만감을 가질 수 있다.
    no_water_dp[0] = True # 초기화
    for i in range(t+1):
        if no_water_dp[i]:
            if i+a <= t:
                no_water_dp[i+a] = True
            if i+b <= t:
                no_water_dp[i+b] = True
    water_dp = [False]*(t+1)
    for i in range(t+1):
        if no_water_dp[i]:
            water_dp[i//2] = True
    for i in range(t+1):
        if water_dp[i]:
            if i+a <= t:
                water_dp[i+a] = True
            if i+b <= t:
                water_dp[i+b] = True
    for i in range(t, -1, -1):
        if water_dp[i]:
            print(i)
            break
solution()