import sys
input = sys.stdin.readline

def backtracking(cnt):
    global flag

    if cnt == 3:
        if bfs():
            flag = True
            return
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == "X":
                    graph[i][j] = "O"
                    backtracking(cnt + 1)
                    graph[i][j] = "X"

def bfs():
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for x, y in teachers:
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            while 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 'O':
                if graph[nx][ny] == "S":
                    return False
                nx += dx
                ny += dy
    return True

N = int(input())
graph = []
teachers = []
flag = False

for i in range(N):
    M = list(map(str, input().rstrip().split(" ")))
    graph.append(M)
    for j in range(N):
        if graph[i][j] == "T":
            teachers.append((i, j))

backtracking(0)

if flag:
    print("YES")
else:
    print("NO")