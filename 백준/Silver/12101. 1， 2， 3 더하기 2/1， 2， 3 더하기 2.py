import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    result = []
    cnt = 0
    def backtracking(total):
        nonlocal cnt
        # 합이 n을 초과하면 더 이상 탐색하면 안됌 (가지치기 필수!)
        if total > n:
            return
        if total == n:
            cnt += 1
            if cnt == k:
                print('+'.join(map(str, result)))
                sys.exit()
            return
        for num in [1,2,3]:
            result.append(num)
            backtracking(total+num)
            result.pop()
    backtracking(0)
    print(-1)
solution()