import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    stars = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'X':
                stars.append((i, j))
    # 각 열별로(둘 다 배열로 선언해서 열 맞추기) 가장 낮은 유성과 가장 높은 땅의 위치 찾기
    lowest_meteor = [-1]*m # 제일 숫자가 높아야 낮은 것
    highest_ground = [n]*m # 제일 숫자가 작아야 높은 것

    # 이동 가능 거리 찾기
    min_go = float('inf')
    for j in range(m):
        for i in range(n):
            if board[i][j] == 'X':
                lowest_meteor[j] = i
            elif board[i][j] == '#':
                highest_ground[j] = i
                break
    
    min_diff = float('inf')
    for j in range(m):
        # 유성이 있을 때만
        if lowest_meteor[j] != -1:
            min_diff = min(min_diff, highest_ground[j]-lowest_meteor[j]-1)
    
    # 원래 있던 유성 모두 없애고 새로 찍기
    for sx, sy in stars:
        board[sx][sy] = '.'
        
    for sx, sy in stars:
        board[sx+min_diff][sy] = 'X'

    for row in board:
        print("".join(row))
solution()