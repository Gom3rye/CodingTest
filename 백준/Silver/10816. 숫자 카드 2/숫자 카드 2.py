import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
def solution():
    n = int(input()) # <= 500,000
    nums = sorted(map(int, input().split()))
    m = int(input()) # <= 500,000
    cnts = list(map(int, input().split()))
    answer = [0]*m
    for i in range(m):
        number = cnts[i]
        answer[i] = bisect_right(nums, number)-bisect_left(nums, number)
    print(*answer)
solution()