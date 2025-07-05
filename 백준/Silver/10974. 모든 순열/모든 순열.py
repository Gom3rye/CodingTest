import sys
input = sys.stdin.readline
from itertools import permutations
def solution():
    n = int(input())
    arr = [i for i in range(1, n+1)]
    for i in permutations(arr, n):
        print(*i)
solution()