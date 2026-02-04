import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    # ladder과 snakes의 이동 역시 어쨌든 시작 -> 도착 정보니까 하나의 정보로 합치기
    board = {} # board = [[] for _ in range(101)]
    for _ in range(n+m):
        start, dest = map(int, input().split())
        board[start] = dest

    visited = [-1]*101
    def bfs(start):
        q = deque([start])
        visited[start] = 0
        while q:
            now = q.popleft()
            if now == 100:
                print(visited[now])
                return
            # 주사위 눈금 1~6까지 모두 탐색
            for dice in range(1, 7):
                nxt = now+dice
                # 보드 범위 넘어가면 안됨
                if nxt > 100:
                    continue
                # 다음 칸이 사다리나 뱀인지 확인 (이때는 텔레포트 개념이므로 거리 +1 안해줘도 된다.)
                if nxt in board:
                    nxt = board[nxt]
                # 이동할 칸이 방문하지 않은 곳이라면 방문할 수 있다.
                if visited[nxt] == -1:
                    visited[nxt] = visited[now]+1
                    q.append(nxt)
            
    bfs(1)
solution()