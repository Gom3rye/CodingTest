import sys
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m = map(int, input().split()) # #사람 <=1000, #가로 칸 <=1000
    lengths = list(int(input()) for _ in range(n))
    # 최소 제곱합 구하기
    # dp[i] = i번째 이름부터 n번째 이름까지 쓸 때의 최소 비용
    dp = [INF]*(n+1)
    dp[-1] = 0 # 마지막 줄은 계산 안한다고 했으므로 끝까지 쓴 최소 비용은 0
    # dp[n] = 쓸 이름이 하나도 남아있지 않은 상태
    for i in range(n-1, -1, -1):
        used = 0
        for j in range(i, n): # i~n-1번째 사람
            # 한 줄에 i~j번째 단어 쓰기
            used += lengths[j]
            # 한 줄에 2단어 이상 쓰면 공백 +1 해줘야 함
            if j > i:
                used += 1
            # 한 줄에 쓴 사람 이름의 길이가 m을 넘으면 안됨
            if used > m:
                break
            # 한 줄을 끝까지 채웠다면
            if j == n-1:
                cost = 0
            else:
                cost = (m-used)**2
            dp[i] = min(dp[i], cost+dp[j+1])
    print(dp[0])
solution()