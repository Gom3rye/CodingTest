import sys
input = sys.stdin.readline
def solution():
    # 최소 횟수로 요리해서 모든 주문 처리하기
    n, m = map(int, input().split()) # #짜장면 <=10,000, #웍 <=100
    woks = list(map(int, input().split())) # 웍의 크기
    # 한 번에 만들 수 있는 모든 그릇 수 = 동전, n을 만드는 최소 동전 개수 dp!!!
    INF = float('inf')
    dp = [INF]*(n+1)
    possible = set() # 한 번에 만들 수 있는 그릇 수
    for wok in woks:
        possible.add(wok)
    for i in range(m): # 양손을 써서 한 번에 만들 수 있는 그릇 수
        for j in range(i+1, m):
            possible.add(woks[i]+woks[j])
    dp[0] = 0 # 0번으로 만들 수 있는 그릇 수는 0개 (초기화)
    # i: 만들 수 있는 그릇 수
    for i in range(1, n+1):
        for dish in possible:
            if i >= dish:
                dp[i] = min(dp[i], dp[i-dish]+1)
    print(dp[n] if dp[n] != INF else -1)  
solution()