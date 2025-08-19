import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    # 0: 위험한 칸, 1: 안전한 칸
    left = [0]+list(map(int, input().strip())) # 1based index로
    right = [0]+list(map(int, input().strip())) # 문자열 숫자로 바꿔주기 주의!
    # n칸을 초과해서 이동하면 게임 클리어
    # 이동할 수 있는 경우의 수 left+1, left-1, left<->right+k
    # 필요한 정보: left/right 여부, 현재 칸
    visited = [[False]*(n+1) for _ in range(2)]
    # left: 0, right: 1
    q = deque([(0, 1, 0)])
    visited[0][1] = True
    while q:
        line, now, time = q.popleft()
        for nline, nxt in [(line, now+1), (line,now-1), (line^1, now+k)]:
            if nxt > n:
                print(1)
                return
            # time+1초에 time+1 칸이 없어지니까
            if nxt <= time+1:
                continue
            elif 1<=nxt<=n and not visited[nline][nxt]:
                if nline == 0 and left[nxt] == 0:
                    continue
                elif nline == 1 and right[nxt] == 0:
                    continue
                visited[nline][nxt] = True
                q.append((nline, nxt, time+1))
    print(0)
solution()