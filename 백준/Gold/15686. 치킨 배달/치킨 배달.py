import sys
from itertools import combinations

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    
    home, chicken = [], []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                home.append((i, j))
            elif city[i][j] == 2:
                chicken.append((i, j))

    # 🔧 모든 집-치킨집 거리 사전 계산
    dist_map = [[abs(hx-cx) + abs(hy-cy) for cx, cy in chicken] for hx, hy in home]

    total_city_dist = float('inf')
    for ch_idx in combinations(range(len(chicken)), m):
        city_dist = 0
        for h in range(len(home)):
            min_dist = float('inf')
            for ci in ch_idx:
                min_dist = min(min_dist, dist_map[h][ci])
            city_dist += min_dist
        total_city_dist = min(total_city_dist, city_dist)

    print(total_city_dist)

solution()