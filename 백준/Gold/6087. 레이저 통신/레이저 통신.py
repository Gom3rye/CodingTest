from collections import deque
import sys
input=sys.stdin.readline

W,H=map(int,input().split())
lst=tuple(list(input()) for _ in range(H))
visit=tuple([0]*W for _ in range(H))
dv=((-1,0),(1,0),(0,-1),(0,1)) #상하좌우 0123
dv_dic={0:(0,2,3),1:(1,2,3),2:(0,1,2),3:(0,1,3),4:(0,1,2,3)} #이전 이동방향에 따라 현재 어디로 방향을 바꿀 수 있는지를 dictionary로 저장
C_rot=[]
for Y in range(H):
        for X in range(W):
            if lst[Y][X]=='C':
                C_rot.append((Y,X))
y,x=C_rot[0]
min_n=10000
queue=deque()
queue.append((y,x,4,0)) # 0은 방문 구분, chg=거울개수+1개를 의미, 4번은 초기화
visit[y][x]=1 #첫 시작점은 1로 초기화
while queue:
    y,x,dir,chg=queue.popleft()
    if (y,x)==C_rot[1]:
        min_n=min(min_n,chg)
        break
    for i in dv_dic[dir]:
        a=chg
        dy=y+dv[i][0]
        dx=x+dv[i][1]
        if dir!=i: #만약 방향을 바꾼다면 거울 +1
            a+=1
        while True:
            if 0<=dy<H and 0<=dx<W and lst[dy][dx]!='*': # 벽이 아니거나 dy, dx가 범위 이내라면 
                if not visit[dy][dx]: # 방문한 적이 없다면
                    visit[dy][dx]=a  # 현재 만난 거울의 수를 저장 
                    queue.append((dy,dx,i,a))
                dy+=dv[i][0] #레이저이므로 쭉 직진
                dx+=dv[i][1]
            else:
                break
print(min_n-1)