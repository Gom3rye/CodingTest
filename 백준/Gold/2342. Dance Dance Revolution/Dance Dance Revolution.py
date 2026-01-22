import sys
INF = float('inf')
input = sys.stdin.readline
def solution():
    arr = list(map(int, input().split()))[:-1] # <100,000
    # 특정 스텝에 도달했을 때 발의 위치 조합에 따라 이후의 최소 비용이 달라짐
    # -> 모든 위치 조합에 대한 최소 힘을 누적해나가야 함
    dp = {(0,0): 0} # 첫 left,right: 비용
    def move(a, b): # prev, nxt
        if a == b: # 같은 곳을 누른다면
            return 1
        elif a == 0: # 0에서 출발한다면
            return 2
        elif abs(a-b) == 2: # 반대편
            return 4
        else:
            return 3
    for op in arr:
        new_dp = {}
        for (left, right), cost in dp.items():
            # 왼쪽을 움직이는 경우
            if op != right:
                new_cost = cost+move(left, op)
                if (op, right) not in new_dp or new_dp[(op, right)] > new_cost:
                    new_dp[(op, right)] = new_cost
            # 오른쪽을 움직이는 경우
            if op != left:
                new_cost = cost+move(right, op)
                if (left, op) not in new_dp or new_dp[(left, op)] > new_cost:
                    new_dp[(left, op)] = new_cost

        dp = new_dp
    print(min(dp.values()))
solution()