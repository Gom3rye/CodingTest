import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input())
    q = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            if q: # 비어있지 않은 경우
                print(-heapq.heappop(q))
            else:
                print(0)
        else:
            heapq.heappush(q, -x)
solution()