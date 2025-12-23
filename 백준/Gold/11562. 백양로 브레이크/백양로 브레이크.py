import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #건물 <=250, #길 <=n(n-1)/2
    INF = float('inf')
    # connected[i][j]: i->j로 연결되기 위해 특정 도로를 양방향 도로로 고쳐야 하는 개수
    connected = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        connected[a][b] = 0
        if c == 0: # 일반통행인 경우
            connected[b][a] = 1
        else: # 양방향인 경우
            connected[b][a] = 0
    for i in range(1, n+1):
        connected[i][i] = 0
    k = int(input()) # #질문 <=30,000
    # 최소 몇 개의 길을 양방향으로 바꿔야 s->e로 도착할 수 있는지 출력
    # 연결 관계 floyd로
    def floyd():
        for k in range(1, n+1):
            for a in range(1, n+1):
                for b in range(1, n+1):
                    connected[a][b] = min(connected[a][b], connected[a][k]+connected[k][b])   
    floyd()
    for _ in range(k):
        s, e = map(int, input().split())
        print(connected[s][e])
solution()