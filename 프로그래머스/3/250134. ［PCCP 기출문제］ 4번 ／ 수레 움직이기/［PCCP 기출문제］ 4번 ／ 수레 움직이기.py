from collections import deque
def solution(maze):
    n, m = len(maze), len(maze[0])
    red_visited = [[False]*m for _ in range(n)]
    blue_visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                srx, sry = i, j
                red_visited[i][j] = True
            elif maze[i][j] == 2:
                sbx, sby = i, j
                blue_visited[i][j] = True
            elif maze[i][j] == 3:
                erx, ery = i, j
            elif maze[i][j] == 4:
                ebx, eby = i, j
    q = deque([((srx, sry, sbx, sby), red_visited, blue_visited, 0)])
    visited = set()
    visited.add((srx, sry, sbx, sby))
    while q:
        (rx, ry, bx, by), red_visited, blue_visited, time = q.popleft()
        red_arrived = (rx, ry) == (erx, ery)
        blue_arrived = (bx, by) == (ebx, eby)
        if red_arrived and blue_arrived:
            return time
        # r/b중 도착한 수레가 있다면 그 수레는 항상 그 자리를 지켜야 한다.
        red_candidates = [(rx, ry)] if red_arrived else []
        if not red_arrived:
            for nx, ny in [(rx+1,ry),(rx-1,ry),(rx,ry+1),(rx,ry-1)]:
                if 0<=nx<n and 0<=ny<m and maze[nx][ny] != 5 and not red_visited[nx][ny]:
                    red_candidates.append((nx, ny))
        blue_candidates = [(bx, by)] if blue_arrived else []
        if not blue_arrived:
            for nx, ny in [(bx+1,by),(bx-1,by),(bx,by+1),(bx,by-1)]:
                if 0<=nx<n and 0<=ny<m and maze[nx][ny] != 5 and not blue_visited[nx][ny]:
                    blue_candidates.append((nx, ny))
                    
        for nrx, nry in red_candidates:
            for nbx, nby in blue_candidates:
                # 동시에 두 수레를 같은 칸으로 움직일 수 없다.
                if (nrx, nry) == (nbx, nby):
                    continue
                # 수레끼리 자리를 바꾸면 안된다.
                if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):
                    continue
                # 새로운 방문배열
                nred_visited = [row[:] for row in red_visited]
                nblue_visited = [row[:] for row in blue_visited]
                nred_visited[nrx][nry] = True
                nblue_visited[nbx][nby] = True
                # 중복 방문 안된다.
                state = (nrx, nry, nbx, nby)
                if state not in visited:
                    visited.add(state)
                    q.append((state, nred_visited, nblue_visited, time+1))
    return 0 # 도달할 수 없는 경우
    