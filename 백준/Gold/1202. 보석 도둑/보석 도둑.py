import sys, heapq
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split()) # 보석 개수, 가방 개수
    # m, v (무게, 가격)
    jewelry = [list(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]
    jewelry.sort() # 무게 기준 오름차순
    bags.sort() # 용량 기준 오름차순
    result = 0
    q = [] # 가격 저장용 최대 힙
    j = 0 # 보석 인덱스
    for bag in bags:
        # 현재 가방에 넣을 수 있는 보석을 힙에 추가
        while j < n and jewelry[j][0] <= bag:
            heapq.heappush(q, -jewelry[j][1]) # 최대 가격을 구해야 하니까 max_heap을 이용 -> 음수로 저장
            j += 1
        # 가장 가치가 높은 보석을 담는다.
        if q:
            result += -heapq.heappop(q)
    print(result)
solution()