import heapq
import sys
input = sys.stdin.readline
n = int(input())

pq = [] #우선순위 큐 초기화
for i in range(n):
    cards = int(input())
    heapq.heappush(pq, cards)
result = 0
while len(pq) != 1:
    one = heapq.heappop(pq)
    two = heapq.heappop(pq)
    sum_val = one + two
    result += sum_val
     # 더 한 결과도 업데이트 해주고
    heapq.heappush(pq, sum_val)

print(result)