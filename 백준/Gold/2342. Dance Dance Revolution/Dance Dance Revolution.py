import sys
input = sys.stdin.readline
def solution():
    numbers = list(map(int, input().split())) # len <= 100,000
    numbers.pop() # 마지막 원소 제거
    # 그 직전의 dp 값만 보면 최소의 파워를 구할 수 있다.
    # dp[left][right]: 두 발이 (l, r)에 있을 때의 최소 힘
    INF = float('inf')
    dp = [[INF]*5 for _ in range(5)]
    # dp 초기화
    dp[0][0] = 0
    def cost(prev, nxt):
        if prev == nxt:
            return 1
        elif prev == 0:
            return 2
        elif abs(prev-nxt) == 2: # 마주보는 경우
            return 4
        else:
            return 3
        
    for nxt in numbers:
        new_dp = [[INF]*5 for _ in range(5)]
        for left in range(5):
            for right in range(5):
                if dp[left][right] == INF: # 접근 불가
                    continue
                # 왼발을 움직이는 경우
                if nxt != right: # 두 발이 같은 곳일 수 없음
                    new_dp[nxt][right] = min(new_dp[nxt][right], dp[left][right]+cost(left, nxt))
                # 오른발을 움직이는 경우
                if nxt != left:
                    new_dp[left][nxt] = min(new_dp[left][nxt], dp[left][right]+cost(right, nxt))
        dp = new_dp
    # 최솟값 출력
    answer = min(min(row) for row in dp)
    print(answer)
solution()