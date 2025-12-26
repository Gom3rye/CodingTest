import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #행성 <=100,000
    # 모든 행성을 터널로 연결하는데 필요한 최소 비: MST
    parents = list(range(n))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parents[b] = a
    edges = []
    # nC2는 시간초과지만 cost는 각 축을 기준으로 했을 때 차가 최소가 되면 되니까 각 축을 기준으로 정렬 후 이웃한 행성들끼리만 비교하면 된다.
    planets = [list(map(int, input().split()))+[p] for p in range(n)]
    for axis in range(3): # x, y, z
        planets.sort(key=lambda x: x[axis])
        for i in range(n-1):
            p1 = planets[i]
            p2 = planets[i+1]
            cost = min(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]), abs(p1[2]-p2[2]))
            edges.append((cost, p1[-1], p2[-1])) # planet의 idx 넣기
    edges.sort()
    answer = 0
    for cost, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            answer += cost
    print(answer)
solution()