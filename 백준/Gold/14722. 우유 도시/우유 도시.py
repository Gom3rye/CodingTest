import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 영역 크기 <=1000
    board = [list(map(int, input().split())) for _ in range(n)]
    # 0:딸기, 1:초코, 2:바나나, 0>1>2>0>1>2... 반복
    # (0,0)~(n-1,n-1)까지 가는데 마실 수 있는 최대 우유 개수 구하기
    dp = [[0]*(n+1) for _ in range(n+1)] # 오른쪽, 아래쪽으로만 갈 수 있다.
    # 다음에 마실 우유 = (마신 개수 % 3)
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 안 마시고 가는 경우
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            # 마시는 경우
            if (dp[i][j]%3) == board[i-1][j-1]:
                dp[i][j] += 1
    print(dp[-1][-1])
solution()