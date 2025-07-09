import sys
input = sys.stdin.readline
from collections import deque
def bfs(hx, hy, fx, fy, seven11, n):
    q = deque([(hx, hy)])
    visited = [False]*n
    while q:
        x, y = q.popleft()
        if abs(x-fx)+abs(y-fy) <= 1000: # 1000까지의 거리는 20병으로 갈 수 있음
            print("happy")
            return
        # 20 병으로 못 가면 편의점 들려야 한다.
        for i in range(n):
            if not visited[i]:
                nx, ny = seven11[i] # 편의점 좌표 뽑기
                if abs(x-nx)+abs(y-ny) <= 1000:
                    visited[i] = True # 편의점 방문
                    q.append((nx, ny))
    print("sad")
    return
def solution():
    t = int(input())
    for _ in range(t):
        n = int(input()) # 편의점의 개수
        hx, hy = map(int, input().split()) # 집 좌표
        seven11 = []
        for _ in range(n):
            cx, cy = map(int, input().split())
            seven11.append((cx, cy)) # 편의점 좌표
        fx, fy = map(int, input().split()) # 페스티벌 좌표
        bfs(hx, hy, fx, fy, seven11, n)
solution()