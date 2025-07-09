import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(hx, hy, fx, fy, seven11, n, visited):
    if abs(hx-fx)+abs(hy-fy) <= 1000:
        return True
    for i in range(n):
        if not visited[i]:
            nx, ny = seven11[i]
            if abs(hx-nx)+abs(hy-ny) <= 1000:
                visited[i] = True
                if dfs(nx, ny, fx, fy, seven11, n, visited):
                    return True
    return False
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
        visited = [False]*n
        if dfs(hx, hy, fx, fy, seven11, n, visited):
            print("happy")
        else:
            print("sad")
solution()