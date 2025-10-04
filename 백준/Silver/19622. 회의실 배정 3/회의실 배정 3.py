import sys
input = sys.stdin.readline
def solution():
    # N개의 회의를 회의실에 효율적으로 배정해 회의를 진행할 수 있는 최대 인원 구하기
    n = int(input())
    # 시작 시간, 끝나는 시간, 회의 인원
    meetings = [list(map(int, input().split())) for _ in range(n)]
    dp = [0]*n # dp[i] = i번째 회의를 듣고 얻을 수 있는 최대 인원
    dp[0] = meetings[0][2]
    if n > 1:
        dp[1] = max(dp[0], meetings[1][2])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+meetings[i][2])
    print(dp[-1])
solution()