import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    n = int(input()) # <= 500,000
    nums = list(map(int, input().split()))
    m = int(input()) # <= 500,000
    cnts = list(map(int, input().split()))
    counter = Counter(nums)
    answer = [0]*m
    for i in range(m):
        answer[i] = counter[cnts[i]]
    print(*answer)
solution()