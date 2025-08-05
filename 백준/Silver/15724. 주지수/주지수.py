import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    ppl = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    dp = [[0]*(m+1) for _ in range(n+1)] # dp[x][y] = (1,1)~(x,y)까지의 누적합
    # dp 초기화
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1] + ppl[i-1][j-1] #ppl은 0based index니까
    result = []
    for i in range(k):
        # 이때 k 수가 많으므로 dp를 1based index로 바꿔주는게 더 낫다.
        x1, y1, x2, y2 = map(int, input().split())
        total = dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]
        result.append(str(total))
    print("\n".join(result))
solution()