import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 객차 수 <= 5만
    customers = [0]+list(map(int, input().split())) # 객차당 손님 수
    a = int(input()) # 끌 수 있는 객차 수
    # 3개의 기관차 있고 각각이 연달아 a개의 객차를 끌 수 있다. -> 최대 손님 수 구하기
    dp = [[0]*(n+1) for _ in range(4)] # dp[i][j]: i개의 기관차가 j번 객차까지 끌었을 때 최대 손님 수
    # 연속된 a개의 합을 구하기 -> 누적합 (j-a+1에서 j번째의 합을 O(1)로 구할 수 있다.)
    prefix_sum = [0]*(n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1]+customers[i]
    for i in range(1, 4):
        for j in range(a, n+1):
            ppl = prefix_sum[j]-prefix_sum[j-a]
            # i번 기관차가 j를 포함하지 않음, 마지막으로 포함함
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-a]+ppl)
    print(dp[-1][-1])
solution()