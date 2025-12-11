import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 도시의 개수 <=20
    graph = [list(map(int, input().split())) for _ in range(n)]
    needed = [[True]*n for _ in range(n)]
    def floyd():
        for k in range(n):
            for a in range(n):
                for b in range(n):
                    if a == b or k == a or k == b:
                        continue
                    # 최소 거리가 아닌 경우 -1 출력
                    if graph[a][b] > graph[a][k]+graph[k][b]:
                        print(-1)
                        sys.exit()
                    # 최단 거리가 같다면 불필요한 도로
                    if graph[a][b] == graph[a][k]+graph[k][b]:
                        needed[a][b] = False
    floyd()
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            if needed[i][j]: # 참이라면 필요한 도로
                total += graph[i][j]
    print(total)
solution()