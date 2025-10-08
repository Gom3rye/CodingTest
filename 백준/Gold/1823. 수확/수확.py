import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    rice = [int(input()) for _ in range(n)]
    # 가장자리에만 벼를 수확해서 얻는 최대 이익
    dp = [[0]*n for _ in range(n)] # dp[i][j]: i번째부터 j번째 벼가 남았을 때의 최대 이익
    for length in range(1, n+1): # length: 계산할 구간의 길이 (남아있는 벼의 개수)
        # 시작점
        for i in range(n-length+1):
            # 끝점
            j = i+length-1
            # k: 현재 수확 순서
            k = n-(j-i) # (전체 n개 - 남은 length개)만큼 수확했으므로 +1
            if i == j:
                dp[i][j] = rice[i]*k
                continue
            # 왼쪽, 오른쪽 수확
            left = rice[i]*k+dp[i+1][j]
            right = rice[j]*k+dp[i][j-1]
            dp[i][j] = max(left, right)
    print(dp[0][n-1])
solution()
