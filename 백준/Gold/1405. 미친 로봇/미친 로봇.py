import sys
input = sys.stdin.readline
def solution():
    n, ep, wp, sp, np = map(int, input().split()) # 이동횟수, 동,서,남,북으로 이동할 확률
    probs = [ep/100, wp/100, sp/100, np/100]
    directions = [(0,1),(0,-1),(1,0),(-1,0)] # 동북서남
    visited = [[False]*29 for _ in range(29)] # 동북서남으로 14칸씩 갈 수 있으니까
    total_prob = 0.0 # probabilities of simple paths
    def backtracking(idx, x, y, prob):
        nonlocal total_prob
        if idx == n:
            total_prob += prob
            return
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = dx+x, dy+y
            # 갈 확률이 0이면 패쓰
            if probs[i] == 0:
                continue
            # 이미 간 곳이면 패쓰 (simple path가 되기 위해서는 안 간 곳만 가야 함)
            if visited[nx][ny]:
                continue
            # 이동
            visited[nx][ny] = True
            backtracking(idx+1, nx, ny, prob*probs[i])
            visited[nx][ny] = False

    visited[14][14] = True # make start point True
    backtracking(0, 14, 14, 1.0) # 첫 시작 좌표는 (14, 14)로 중간에서 시작, initial prob = 1.0
    print(total_prob)
solution()