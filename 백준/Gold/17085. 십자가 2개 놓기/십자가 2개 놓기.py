import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 2<= <=15
    board = [[1 if c=='#' else 0 for c in input().strip()] for _ in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    # 한 점에서 가능한 최대 크기 구하기
    def get_max_size(x, y):
        size = 0
        while True:
            for dx, dy in directions:
                nx, ny = x+dx*size, y+dy*size
                if not(0<=nx<n and 0<=ny<m and board[nx][ny] == 1):
                    return size-1
            size += 1
    # 십자가가 겹치는지 확인하기 위해 좌표들 다 set으로 저장해놓기
    def get_cells(x, y, size):
        cells = {(x, y)}
        for s in range(1, size+1):
            for dx, dy in directions:
                nx, ny = x+dx*s, y+dy*s
                cells.add((nx, ny))
        return cells
    # 십자가 완전탐색으로 구해보기
    crosses = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                max_size = get_max_size(i, j)
                for s in range(max_size+1):
                    area = 1+4*s
                    cells = get_cells(i, j, s)
                    crosses.append((area, cells))
    # 두 십자가의 크기 곱 최대값 구하기
    answer = 0
    for i in range(len(crosses)):
        area1, cells1 = crosses[i]
        for j in range(i+1, len(crosses)):
            area2, cells2 = crosses[j]
            if cells1.isdisjoint(cells2): # cross1의 좌표들과 cross2의 좌표들이 겹치지 않는다면
                answer = max(answer, area1*area2)
    print(answer)
solution()