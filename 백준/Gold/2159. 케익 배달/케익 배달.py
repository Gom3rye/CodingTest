import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    sx, sy = map(int, input().split())
    customers = [list(map(int, input().split())) for _ in range(n)]
    dp = {(sx, sy): 0}

    for cx, cy in customers:
        next_dp = {}
        delivery_spots = [(cx, cy), (cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]
        
        for nx, ny in delivery_spots:
            min_d = float('inf')
            for (px, py), pdist in dp.items():
                dist = pdist + abs(nx-px) + abs(ny-py)
                min_d = min(min_d, dist)
            next_dp[(nx, ny)] = min_d
        dp = next_dp
    print(min(dp.values()))
solution()