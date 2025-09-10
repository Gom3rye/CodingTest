import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # n*n격자, m번의 이동
    a = [list(map(int, input().split())) for _ in range(n)]
    directions = {1:(0,-1), 2:(-1,-1), 3:(-1,0), 4:(-1,1), 5:(0,1), 6:(1,1), 7:(1,0), 8:(1,-1)}
    # 행, 열 연결되었으니 % 연산하기
    dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]
    def move(a, init_cloud, d, s):
        # 새로운 구름좌표를 저장해놓는 배열
        clouds = []
        for cx, cy in init_cloud:
            dx, dy = directions[d]
            nx, ny = (cx+dx*s)%n, (cy+dy*s)%n
            clouds.append((nx, ny)) # 새로운 구름 표시
        
        # 또 다음 새로운 구름좌표에 지금 새로운 구름좌표가 포함되지 않도록
        visited = [[False]*n for _ in range(n)]
        for x, y in clouds:
            visited[x][y] = True
            a[x][y] += 1 # 비가 내려서 1증가

        # 물복사 마법
        for x, y in clouds:
            cnt = 0
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n and a[nx][ny] != 0:
                    cnt += 1
            # 물복사만큼 증가
            a[x][y] += cnt
        
        # 2이상인 새로운 구름 만들기
        new_clouds = []
        for i in range(n):
            for j in range(n):
                if a[i][j] >= 2 and not visited[i][j]:
                    new_clouds.append((i, j))
                    a[i][j] -= 2
        # print(f"a: {a}, new_clouds: {new_clouds}")
        return a, new_clouds


    init_cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
    for _ in range(m): # 명령
        d, s = map(int, input().split())
        new_a, new_clouds = move(a, init_cloud, d, s)
        init_cloud = new_clouds
        a = new_a

    # 바구니에 들어있는 물의 양의 합 출력
    result = 0
    for row in a:
        result += sum(row)
    print(result)
solution()