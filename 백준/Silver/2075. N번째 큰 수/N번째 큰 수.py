import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input()) # n*n표, n번째 큰 수 <=1500
    q = []
    for _ in range(n):
        numbers = list(map(int, input().split()))
        for num in numbers:
            heapq.heappush(q, num)

        while len(q) > n:
            heapq.heappop(q)
    print(q[0])
solution()