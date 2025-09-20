import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 가능한 모든 비밀번호의 개수를 구하는 것, 백트레킹
    visited = [False]*10
    for num in numbers:
        visited[num] = True
    cnt = 0
    def backtracking(idx, partial):
        nonlocal cnt
        if idx == n:
            if partial == m:
                cnt += 1
            return
        for num in range(10):
            if not visited[num]:
                backtracking(idx+1, partial)
            else:
                visited[num] = False
                backtracking(idx+1, partial+1)
                visited[num] = True

    backtracking(0, 0)
    print(cnt)
solution()