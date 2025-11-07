#백준 14948번 군대탈출하기
from heapq import heappop,heappush
import sys

dx=[0,0,1,-1]
dy=[1,-1,0,0]

N,M=map(int,input().split())

room=[list(map(int,input().split()))for _ in range(N)]
visited=[[[sys.maxsize]*2 for _ in range(M)]for _ in range(N)]
visited[0][0][0]=room[0][0]
q=[]
heappush(q,[0,0,0])


answer=1e9

while q:
    x,y,use=heappop(q)
    level=visited[x][y][use]

    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        now_level=max(room[nx][ny],level)
        if visited[nx][ny][use]>now_level:
            visited[nx][ny][use]=now_level
            heappush(q,[nx,ny,use])

        if use==0:
            nx+=dx[d]
            ny+=dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            now_level = max(room[nx][ny], level)
            if visited[nx][ny][use+1]>now_level:
                visited[nx][ny][use+1] = now_level
                heappush(q, [ nx, ny, use+1])

print(min(visited[N-1][M-1]))