import sys
INF = float('inf')
input = sys.stdin.readline
def solution():
    arr = list(map(int, input().split()))[:-1]
    n = len(arr) # <100,000
    # 최소의 힘 출력 (특정 스텝에 도달했을 때 발의 위치 조합에 따라 이후의 최소 비용이 달라짐)
    # -> 모든 위치 조합에 대한 최소 힘을 누적해나가야 함
    dp = [[INF]*5 for _ in range(5)] # dp[idx][left][right]을 new_dp, dp 2개를 이용해서 2차원으로 대체
    def move(a, b): # prev, nxt
        if a == b: # 같은 곳을 누른다면
            return 1
        elif a == 0: # 0에서 출발한다면
            return 2
        elif abs(a-b) == 2: # 반대편
            return 4
        else:
            return 3
    dp[0][0] = 0 # 첫 비용 초기화
    for op in arr:
        new_dp = [[INF]*5 for _ in range(5)]
        for left in range(5):
            for right in range(5):
                if dp[left][right] == INF: # 최적화를 위해
                    continue
                # 왼쪽을 움직이는 경우
                if op != right: # 두 발이 같은 곳에 가면 안되니까
                    new_dp[op][right] = min(new_dp[op][right], dp[left][right]+move(left, op))
                # 오른쪽을 움직이는 경우
                if op != left: 
                    new_dp[left][op] = min(new_dp[left][op], dp[left][right]+move(right, op))
        dp = new_dp
    print(min(map(min, dp)))
solution()