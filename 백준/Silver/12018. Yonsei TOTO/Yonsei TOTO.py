import sys
from math import log2
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m = map(int, input().split()) # #과목 <=100, 주어진 마일리지 <=100
    candidates = []
    for _ in range(n):
        p, l = map(int, input().split()) # 과목수, 수강인원
        mileage = sorted(map(int, input().split()))
        if p < l:
            candidates.append(1)
        elif p == l:
            candidates.append(mileage[0])
        else: # p > l
            diff = p-l
            candidates.append(mileage[diff])
    candidates.sort()
    cnt, now = 0, 0
    for i in range(len(candidates)):
        now += candidates[i]
        if now > m:
            break
        cnt += 1
    print(cnt)
solution()