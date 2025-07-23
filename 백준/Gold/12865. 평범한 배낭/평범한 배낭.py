import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    bags = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [0]*(k+1)   # dp[i]: 무게가 i일 때 얻을 수 있는 최대 가치를 저장
    # 배낭은 한 번씩만 쓸 수 있으니까 역순으로 계산
    for w, v in bags:
        for weight in range(k, w-1, -1):
            dp[weight] = max(dp[weight], dp[weight-w]+v)
    print(dp[k])
solution()