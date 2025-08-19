# 지도의 크기 입력 받기
n = int(input())

# 지도 정보 입력 받기
map_info = []
for i in range(n):
    map_info.append(list(map(int, input())))

# 방문 여부를 저장할 리스트 생성하기
visited = [[False]*n for _ in range(n)]

# 상하좌우 이동을 위한 dx, dy 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수 정의하기
def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if map_info[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)
                
# 각 단지내 집의 수를 저장할 리스트
counts = []

# 모든 위치에 대해 DFS 수행하기
for i in range(n):
    for j in range(n):
        if map_info[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            counts.append(count)

# 총 단지수와 각 단지내 집의 수를 출력하기
print(len(counts))
counts.sort()
for count in counts:
    print(count)