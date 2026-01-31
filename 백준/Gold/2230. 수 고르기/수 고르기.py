import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #수 <=100,000, target <=2,000,000,000
    arr = sorted(int(input()) for _ in range(n))
    min_diff = float('inf')
    start, end = 0, 1
    while end < n:
        diff = arr[end]-arr[start]
        if diff < m:
            end += 1
        elif diff > m:
            min_diff = min(min_diff, diff)
            start += 1
        else:
            print(m)
            return
    print(min_diff)
solution()