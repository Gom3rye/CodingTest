import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 물건의 개수 <= 100
    m = int(input()) # 물건 쌍의 개수 <= 2000
    # 앞 > 뒤
    reach = [[False]*(n+1) for _ in range(n+1)]
    nodes = []
    for _ in range(m):
        a, b = map(int, input().split())
        reach[a][b] = True
        nodes.append((b, a))
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
                    nodes.append((j, i))
    for b, a in nodes:
        reach[b][a] = True
    for i in range(1, n+1):
        reach[i][i] = True
    # 비교 결과를 모르는 물건의 개수: n-True개수
    for row in reach[1:]:
        print(n-sum(row))
solution()