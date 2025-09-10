import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split()) # n*n격자, 초기체력, 민트초코 마셨을때 증가하는 체력
    board = [list(map(int, input().split())) for _ in range(n)]
    mintchocos = []
    # 순서: 이동 후 마셔서 체력 보충
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hx, hy = i, j # 진우의 집 좌표
            elif board[i][j] == 2:
                mintchocos.append((i, j)) # 민초의 좌표
    mint_n = len(mintchocos)
    # 방문 처리할 배열
    visited = [False]*mint_n
    max_cnt = 0
    def dist(sx, sy, dx, dy):
        return abs(sx-dx)+abs(sy-dy)
    def backtracking(x, y, hp, cnt): # 민트초코 조합으로 뽑는 백트레킹
        nonlocal max_cnt

        if max_cnt == mint_n: # 최대 민트 초코 개수가 전체와 같다면
            return
        
        # 집에 다시 돌아올 수 있는 경우에 max_cnt 값 갱신
        if hp-(abs(hx-x)+abs(hy-y)) >= 0:
            max_cnt = max(max_cnt, cnt)
        
        for i in range(mint_n):
            if not visited[i]:
                mx, my = mintchocos[i] # mint_x, mint_y
                needed = abs(x-mx)+abs(y-my)
                # 지금 당장은 집에 못 돌아가더라도, 앞으로 더 많은 민초를 먹어서 체력을 늘린 후에 집에 돌아갈 수 있다면 괜찮다는 조건 주의!
                if hp >= needed:
                    visited[i] = True
                    backtracking(mx, my, hp-needed+k, cnt+1)
                    visited[i] = False

    backtracking(hx, hy, m, 0)
    print(max_cnt)
solution()