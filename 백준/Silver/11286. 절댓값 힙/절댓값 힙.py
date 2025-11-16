import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input())
    q = []
    for _ in range(n):
        x = int(input())
        if x != 0:
            heapq.heappush(q, (abs(x), x))
        elif x == 0 and q:
            print(heapq.heappop(q)[1])
        else: # x == 0 and q가 비어있을 때:
            print(0)
solution()