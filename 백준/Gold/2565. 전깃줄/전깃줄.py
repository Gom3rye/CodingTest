import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    # a(lines[][0])부분이 정렬이 되어야 하기 때문에 sort
    lines = sorted(list(map(int, input().split())) for _ in range(n))
    b = [lines[i][1] for i in range(n)]
    # n-b의 가장 긴 증가수열 이 정답
    dp = [1]*n # dp[i]: i번째 수까지 봤을 때 가장 긴 증가수열의 길이
    for i in range(1, n):
        for j in range(i): # j: i보다 뒤에 있는 인덱스
            if b[i] > b[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(n-max(dp))
solution()