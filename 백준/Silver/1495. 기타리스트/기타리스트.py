import sys
input = sys.stdin.readline
def solution():
    n, s, m = map(int, input().split()) # 곡 수, 시작 볼륨, 최대 볼륨
    v = list(map(int, input().split()))
    dp = [[False]*(m+1) for _ in range(n+1)] # dp[0]에서 시작해서 dp[n]까지 가야 하니까
    # dp[i][vol]: i번째 곡을 시작할 때 vol이 가능한지 여부
    dp[0][s] = True
    for i in range(n):
        for vol in range(m+1):
            if dp[i][vol]:
                # up
                if vol+v[i] <= m:
                    dp[i+1][vol+v[i]] = True
                # down
                if vol-v[i] >= 0:
                    dp[i+1][vol-v[i]] = True

    for vol in range(m, -1, -1):
        if dp[n][vol]:
            print(vol)
            break
    else:
        print(-1)

solution()