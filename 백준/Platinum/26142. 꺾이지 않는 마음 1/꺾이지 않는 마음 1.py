import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #용 <=10000
    # 키 증가양 <=10^6, 키 <=10^12
    dragons = [list(map(int, input().split())) for _ in range(n)]
    # 성장률이 큰 용을 나중에 베어야 한다. (같은 용을 여러번 베는 것도 가능하지만 최댓값을 구하려면 각각 다른 용을 베는게 낫다.)
    # -> 0/1 knapsack 문제!! (단, 아이템의 가치가 날짜에 따라 변하는 특수한 knapsack-> sort 필요)
    dragons.sort() # 작은 성장률부터 앞자리 채우기
    dp = [0]*(n+1)
    for i in range(n): # 0based index
        d, h = dragons[i]
        for day in range(i+1, 0, -1): # 0/1냅색이니까 뒤에서부터
            dp[day] = max(dp[day], dp[day-1]+h+(day-1)*d)
    print('\n'.join(map(str, dp[1:])))
solution()