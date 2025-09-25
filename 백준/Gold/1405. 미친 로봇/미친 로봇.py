import sys
input = sys.stdin.readline
def solution():
    n, ep, wp, sp, np = map(int, input().split()) # 이동횟수, 동,서,남,북으로 이동할 확률
    probs = [ep/100, wp/100, sp/100, np/100]
    visited = [[False]*29 for _ in range(29)] # 동북서남으로 14칸씩 갈 수 있으니까
    total_prob = 0.0 # probabilities of simple paths
    def backtracking(idx, x, y, prob):
        nonlocal total_prob
        if visited[x][y]: # 이미 방문한 곳이라면 simple path 못되니까 가지치기
            return
        if idx == n:
            total_prob += prob
            return
        visited[x][y] = True
        backtracking(idx+1, x, y+1, prob*probs[0])
        backtracking(idx+1, x, y-1, prob*probs[1])
        backtracking(idx+1, x+1, y, prob*probs[2])
        backtracking(idx+1, x-1, y, prob*probs[3])
        visited[x][y] = False
    backtracking(0, 14, 14, 1.0)
    print(total_prob)
solution()