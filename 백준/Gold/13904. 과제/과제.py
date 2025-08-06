import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    info.sort()
    q = []
    for deadline, task in info:
        heapq.heappush(q, task)
        if len(q) > deadline:
            heapq.heappop(q)
    print(sum(q))
solution()