import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    max_result = 0
    # a의 모든 순열(permutation)을 구함
    for p in permutations(a):
        result = 0
        for i in range(n - 1):
            result += abs(p[i] - p[i+1])
        max_result = max(max_result, result)
    print(max_result)
solution()