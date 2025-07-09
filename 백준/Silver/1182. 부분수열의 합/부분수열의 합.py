import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solution():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0

    def backtracking(idx, total):
        nonlocal count
        if idx == n:
            if total == s:
                count += 1
            return
        # 현재 원소 선택
        backtracking(idx+1, total+nums[idx])
        # 현재 원소 선택 안함
        backtracking(idx+1, total)

    backtracking(0, 0)
    # 예외 처리: S가 0인 경우 공집합도 세어지므로 -1 처리
    print(count if s != 0 else count - 1)

solution()