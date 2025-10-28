import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    p = int(input())
    for _ in range(p):
        board = [] # toggle 하기 쉽게 0(.), 1(*)로
        for _ in range(3):
            row = [1 if tmp == '*' else 0 for tmp in input().strip()]
            board.append(row)
        # 총 9칸밖에 없으므로 (2^9, 누르거나/말거나) 완전탐색 가능
        start = [[0]*3 for _ in range(3)]
        answer = 10 # 최소 클릭 수
        directions = [(0,0),(0,1),(0,-1),(1,0),(-1,0)]
        def click(start, x, y): # 한 칸 클릭시 인접한 토글을 한 함수로 처리 (재귀랑 섞여 있으면 인접한 토글 다 하지도 못한채 새로운 x,y로 토글 도니까 함수로 빼서 원자화 시키기)
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<3 and 0<=ny<3:
                    start[nx][ny] = start[nx][ny]^1 # start[nx][ny] ^= 1
        def backtracking(i, cnt):
            nonlocal answer
            if i == 9:
                if start == board:
                    answer = min(answer, cnt)
                return
            x, y = i//3, i%3  # x, y = divmod(i, 3)
            # 현재 칸 누르거나
            click(start, x, y)
            backtracking(i+1, cnt+1)
            click(start, x, y) # 상태복구

            # 누르지 않거나
            backtracking(i+1, cnt)
        backtracking(0, 0)
        print(answer)
solution()