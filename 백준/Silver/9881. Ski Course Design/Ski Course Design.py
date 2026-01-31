import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #hills <=1000
    hills = [int(input()) for _ in range(n)] # range(0, 101)
    min_hill, max_hill = min(hills), max(hills)
    if max_hill-min_hill <= 17:
        print(0)
        return
    # 최종적으로 모든 언덕 높이가 어떤 [h, h+17]안에 들어가야 함
    # 가능한 높이가 최대 100까지로 충분히 작으므로 h로 완탐돌리기!
    min_cost = float('inf')
    for low in range(0, 84):
        cost = 0
        high = low+17
        for hill in hills:
            if hill < low:
                cost += (low-hill)**2
            elif hill > high:
                cost += (hill-high)**2
        min_cost = min(min_cost, cost)
    print(min_cost)
solution()