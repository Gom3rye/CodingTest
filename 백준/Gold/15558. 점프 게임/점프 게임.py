import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    board = [[0]+list(map(int, input().strip())) for _ in range(2)]
    # 이동할 수 있는 경우의 수 left+1, left-1, left<->right+k
    # 필요한 정보: left/right 여부, 현재 칸
    visited = [[False]*(n+1) for _ in range(2)]
    # left: 0, right: 1
    q = deque([(0, 1, 0)]) # line, now, time
    visited[0][1] = True
    while q:
        line, now, time = q.popleft()
        time += 1
        for nline, nxt in [(line, now+1), (line,now-1), (line^1, now+k)]:
            if nxt > n:
                print(1)
                return
            # time초에 time칸이 없어지니까 nxt는 time보다 커야 하고
            if nxt > time and not visited[nline][nxt] and board[nline][nxt] == 1:
                visited[nline][nxt] = True
                q.append((nline, nxt, time))
    print(0)
solution()