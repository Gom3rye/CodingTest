import sys, heapq
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split()) # 보석 개수, 가방 개수 <=300,000
    # 훔칠 수 있는 보석의 최대 가격 구하기-> 
    jewels = [list(map(int, input().split())) for _ in range(n)] # 무게, 가격
    jewels.sort()
    bags = sorted(int(input()) for _ in range(k))
    # 최대 가격을 담아야 하니까 maxheap 사용해서 큰 후보자들 담아놓고 배정하기
    q = []
    idx = 0
    answer = 0
    for bag in bags:
        while idx < n and jewels[idx][0] <= bag:
            heapq.heappush(q, -jewels[idx][1])
            idx += 1
        if q: # 후보가 있다면 가방에 할당
            answer += -heapq.heappop(q)
    print(answer)
solution()