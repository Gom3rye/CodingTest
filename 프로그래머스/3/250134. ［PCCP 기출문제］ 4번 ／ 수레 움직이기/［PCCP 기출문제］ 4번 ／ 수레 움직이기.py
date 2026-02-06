import sys
sys.setrecursionlimit(10**6)
INF = float('inf')
def solution(maze):
    answer = INF # 최소 횟수
    # R/B가 도착하면 이제 거긴 못 지나감
    n, m = len(maze), len(maze[0])
    # 1->3, 2->4로 가야 한다.
    red_visited = [[False]*m for _ in range(n)]
    blue_visited = [[False]*m for _ in range(n)]
    srx = sry = sbx = sby = -1 # 시작점 초기화
    erx = ery = ebx = eby = -1 # 도착점 초기화
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_visited[i][j] = True
                srx, sry = i, j
            elif maze[i][j] == 2:
                blue_visited[i][j] = True
                sbx, sby = i, j
            elif maze[i][j] == 3:
                erx, ery = i, j
            elif maze[i][j] == 4:
                ebx, eby = i, j
                
    def backtracking(rx, ry, bx, by, time): # 전 rx, ry, bx, by, 시간
        nonlocal answer
        # 가지치기
        if time >= answer:
            return
        
        # 둘다 도착하면 answer 갱신
        red_arrived = (rx, ry) == (erx, ery)
        blue_arrived = (bx, by) == (ebx, eby)
        if red_arrived and blue_arrived:
            answer = min(answer, time)
            return
        
        # r가 갈 수 있는 후보 선정
        red_candidates = [(erx, ery)] if red_arrived else []
        if not red_arrived:
            for nx, ny in [(rx+1,ry),(rx-1,ry),(rx,ry+1),(rx,ry-1)]:
                if 0<=nx<n and 0<=ny<m and not red_visited[nx][ny] and maze[nx][ny] != 5:
                    red_candidates.append((nx, ny))
        # b가 갈 수 있는 후보 선정
        blue_candidates = [(ebx, eby)] if blue_arrived else []
        if not blue_arrived:
            for nx, ny in [(bx+1,by),(bx-1,by),(bx,by+1),(bx,by-1)]:
                if 0<=nx<n and 0<=ny<m and not blue_visited[nx][ny] and maze[nx][ny] != 5:
                    blue_candidates.append((nx, ny))
        
        for nrx, nry in red_candidates:
            for nbx, nby in blue_candidates:
                # 동시에 두 수레를 같은 칸으로 움직일 수 없다.
                if (nrx, nry) == (nbx, nby):
                    continue
                # 수레끼리 자리 swap할 수 없다.
                if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):
                    continue
                
                # 방문 처리
                red_visited[nrx][nry] = True
                blue_visited[nbx][nby] = True
                
                backtracking(nrx, nry, nbx, nby, time+1)
                
                # 상태 복구
                red_visited[nrx][nry] = False
                blue_visited[nbx][nby] = False
        
    backtracking(srx, sry, sbx, sby, 0)
    return answer if answer != INF else 0