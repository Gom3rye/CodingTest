import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #사람 <=10
    # cnt의 idx: idx+1번째 사람의 왼쪽에 자신보다 큰 사람이 있는 횟수
    cnt = list(map(int, input().split()))
    if sum(cnt) == 0:
        print(*range(1, n+1))
        return

    placement = [-1]*n
    def backtracking(idx):
        if idx == 0:
            print(*placement)
            sys.exit()

        for pos in range(n):
            if placement[pos] == -1:
                bigger = 0
                for i in range(pos):
                    if placement[i] != -1:
                        bigger += 1
                if bigger == cnt[idx-1]:
                    placement[pos] = idx
                    backtracking(idx-1)
                    placement[pos] = -1
    backtracking(n)
solution()