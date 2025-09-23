import sys
from itertools import combinations
input = sys.stdin.readline
def solution():
    n, l, r, x = map(int, input().split())
    a = sorted(map(int, input().split()))
    count = 0
    for cnt in range(2, n+1):
        for comb in combinations(a, cnt):
            value = sum(comb)
            # 난이도의 합이 l보다 크거나 같아야 하고 r보다 작거나 같아야 하고
            if value > r or value < l:
                continue
            # 최대값<->최솟값 차이는 x보다 크거나 같아야 한다.
            if comb[-1]-comb[0] < x:
                continue
            count += 1
    print(count)
solution()