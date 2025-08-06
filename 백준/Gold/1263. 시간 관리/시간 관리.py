import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    info.sort(key=lambda x: x[1], reverse=True)
    start = float('inf')
    for time, deadline in info:
        start = min(start, deadline)
        start -= time
        if start < 0:
            print(-1)
            return
    print(start)
solution()