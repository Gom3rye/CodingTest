import sys
input = sys.stdin.readline
from itertools import product
def solution():
    n, m = map(int, input().split())
    arr = sorted(map(int,input().split()))
    for i in product(arr, repeat=m):
        print(*i)

solution()