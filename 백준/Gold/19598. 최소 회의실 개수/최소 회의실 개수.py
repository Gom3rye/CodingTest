import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input()) # 배열의 크기 <=100,000
    info = [list(map(int, input().split())) for _ in range(n)]
    info.sort()
    q = []
    for start, end in info:
        if q and q[0] <= start: # 재활용 가능
            heapq.heappop(q)
        heapq.heappush(q, end)
    print(len(q))
solution()