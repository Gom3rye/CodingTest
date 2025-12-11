import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        k = int(input())
        files = [0]+list(map(int, input().split()))
        dp = [[0]*(k+1) for _ in range(k+1)] # dp[i][j]: i~j까지의 파일을 합칠 때 필요한 최소 비용
        # 최적화를 위해 누적합 구하기
        prefix_sum = [0]*(k+1)
        for i in range(1, k+1):
            prefix_sum[i] = prefix_sum[i-1]+files[i]
        # 구간 길이에 따라
        for length in range(2, k+1): # 2~k+1까지의 수를 더할 수 있다.
            for start in range(1, k-length+2):
                end = start+length-1
                # 최솟값을 구하는 거니까 무한대로 초기화
                dp[start][end] = float('inf')
                # 현재 구간합
                total = prefix_sum[end]-prefix_sum[start-1]
                for mid in range(start, end):
                    dp[start][end] = min(dp[start][end], dp[start][mid]+dp[mid+1][end]+total)
        print(dp[1][k])
solution()