import sys, heapq
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #카드 <=1000, #합체 <=15000
    cards = list(map(int, input().split()))
    # 합체해서 만들 수 있는 가장 작은 수 출력-> 가장 작은 수들끼리 합쳐야 한다.
    heapq.heapify(cards) # cards를 heapq에 넣기
    for _ in range(m):
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        sum_ab = a+b
        heapq.heappush(cards, sum_ab)
        heapq.heappush(cards, sum_ab)
    print(sum(cards))
solution()