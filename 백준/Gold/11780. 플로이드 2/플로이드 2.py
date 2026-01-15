import sys
input = sys.stdin.readline
INF = float('inf')
def solution():
    n = int(input()) # #도시 <=100
    m = int(input()) # #버스 <=100,000
    costs = [[INF]*(n+1) for _ in range(n+1)]
    prev = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        costs[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        costs[a][b] = min(costs[a][b], c)
    def floyd():
        for k in range(1, n+1):
            for a in range(1, n+1):
                for b in range(1, n+1):
                    if costs[a][b] > costs[a][k]+costs[k][b]:
                        costs[a][b] = costs[a][k]+costs[k][b]
                        prev[a][b] = k
    floyd()
    for i in range(1, n+1):
        for j in range(1, n+1):
            if costs[i][j] == INF:
                costs[i][j] = 0
    for cost in costs[1:]:
        print(*cost[1:])
    
    # 재귀로 경로 추적
    def track(i, j):
        if prev[i][j] == 0:
            return [i, j]
        k = prev[i][j]
        return track(i, k)[:-1]+track(k, j) # k는 중복되므로 한 번만 포함
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j or costs[i][j] == 0:
                print(0)
                continue
            path = track(i, j)
            print(len(path), *path)
solution()