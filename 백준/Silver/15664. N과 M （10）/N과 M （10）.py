import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    arr = sorted(map(int, input().split()))
    answer = []
    ans_set = set()
    def backtracking(s):
        if len(answer) == m:
            ans_set.add(tuple(answer))
            return
        for i in range(s, n):
            answer.append(arr[i])
            backtracking(i+1)
            answer.pop()
    backtracking(0)
    for ans in sorted(ans_set):
        print(*ans)
solution()