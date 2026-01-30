import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #벽장 <=20
    open1, open2 = map(int, input().split())
    m = int(input()) # 사용할 벽장 순서의 길이 <=20
    doors = list(int(input()) for _ in range(m))
    # open1을 먼저 여는 경우와 open2를 먼저 여는 경우-> 최대 20번 골라야 하고 같은 조건에서는 항상 같은 결과 도출 => 재귀+memoization하자!
    dp = [[[-1]*(n+1) for _ in range(n+1)] for _ in range(m+1)] # dp[idx][open1][open2]: open1,2가 열린채로 idx번째 벽장이 이동한 최소 횟수
    def move(idx, open1, open2):
        if idx == m:
            return 0 # 끝까지 도달한 거니까 비용 0주면서 리턴
        
        if dp[idx][open1][open2] != -1:
            return dp[idx][open1][open2]
        
        # open1 먼저 채운 상황
        cost1 = abs(open1-doors[idx])+move(idx+1, doors[idx], open2)
        # open2 먼저 채운 상황
        cost2 = abs(open2-doors[idx])+move(idx+1, open1, doors[idx])
        
        dp[idx][open1][open2] = min(cost1, cost2)
        return dp[idx][open1][open2]

    print(move(0, open1, open2))
solution()