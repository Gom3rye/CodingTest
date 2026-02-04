import sys
input = sys.stdin.readline
def solution(k, dungeons):
    # 최대 던전의 수가 8개이므로 백트레킹 가능(순열)
    n = len(dungeons)
    visited = [False]*n
    def backtracking(hp, cnt):
        max_cnt = cnt
        for i in range(n):
            if not visited[i] and dungeons[i][0] <= hp:
                visited[i] = True
                max_cnt = max(max_cnt, backtracking(hp-dungeons[i][1], cnt+1))
                visited[i] = False
        return max_cnt
    return backtracking(k, 0)