import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n = int(input()) # #day <=1000 -> 완탐은 8^1000으로 말도 안됨, dp-> 1000*9 쓰자.
    visited = [[False]*10 for _ in range(n)] # i번째 날에 t떡을 줄 수 있는지/없는지
    tteoks = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        tteoks.append(temp[1:])
    placement = [0]*n
    def backtracking(idx, prev):
        # 마지막까지 무사히 떡을 다 준 경우
        if idx == n:
            return True
        for t in tteoks[idx]:
            if prev != t and not visited[idx][t]:
                placement[idx] = t
                if backtracking(idx+1, t):
                    return True
                visited[idx][t] = True
        return False
    if backtracking(0, 0): # 0떡은 불가능한 경우이므로 더미값으로 넣어주기
        print(*placement, sep='\n')
    else:
        print(-1)
solution()