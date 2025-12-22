import sys
input = sys.stdin.readline
from collections import deque
def solution():
    s = int(input()) # 만들어야 하는 이모티콘 수
    def bfs():
        # 화면, 클립보드, 시간 (화면에 같은 이모티콘 수가 있어도 클립보드에 몇 개가 있냐에 따라 다른 경우의 수가 되므로 셋 다 변수처럼 기록)
        q = deque([(1, 0, 0)])
        visited = [[False]*(s+1) for _ in range(s+1)] # 화면, 클립보드 둘 다 체크하기 위해 2차원 배열로
        visited[1][0] = True # x가 화면, y가 클립보드
        while q:
            screen, clip, time = q.popleft()
            if screen == s:
                print(time)
                return
            # 화면의 이모티콘을 -> 클립보드로
            if not visited[screen][screen]:
                visited[screen][screen] = True
                q.append((screen, screen, time+1))
            # 클립보드의 이모티콘을 -> 화면으로
            if clip > 0 and screen+clip<=s and not visited[screen+clip][clip]: # clip이 비어있으면 붙여넣기 못함
                visited[screen+clip][clip] = True
                q.append((screen+clip, clip, time+1))
            # 이모티콘 화면 -1
            if 2<=screen-1<=s and not visited[screen-1][clip]: # 이모티콘의 개수는 2이상
                visited[screen-1][clip] = True
                q.append((screen-1, clip, time+1))
    bfs()
solution()