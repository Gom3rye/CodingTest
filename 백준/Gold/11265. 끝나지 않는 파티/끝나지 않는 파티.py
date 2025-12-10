import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 파티장 크기 <=500, 서비스 요청한 손님 수 <=10000
    graph = [list(map(int, input().split())) for _ in range(n)]
    def floyd():
        for k in range(n):
            for a in range(n):
                for b in range(n):
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    floyd()
    for _ in range(m):
        a, b, c = map(int, input().split()) # 현재 위치, 가야할 곳, 남은 시간
        if graph[a-1][b-1] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")
solution()