import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    A = list(list(zip(*board))[0])
    B = list(list(zip(*board))[1])
    C = [row[2] for row in board]
    D = [row[3] for row in board]
    # C와 D의 합을 Counter로 한 번에 계산
    sum_cd = Counter(cv+dv for cv in C for dv in D)
    count = 0
    for av in A:
        for bv in B:
            sum_ab = av + bv
            target = -sum_ab
            count += sum_cd[target]
    print(count)
solution()