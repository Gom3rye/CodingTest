import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input()) # 주유소의 개수 <=10000
    infos = []
    for _ in range(n):
        a, b = map(int, input().split()) # 시작~주유소까지 거리 <=1,000,000, 그 주유소에서 채울 수 있는 연료양 <=100
        infos.append((a, b))
    l, p = map(int, input().split()) # 현재~마을까지의 거리, 기존 트럭에 있던 연료양 <= 1,000,000
    infos.sort() # 거리 순으로 정렬 (한 번 지난 곳은 더 지나지 않기 위해)
    q = [] # 얻을 수 있는 기름의 최대 순으로 정렬해야 함 -> max heap
    answer = 0 # 들리는 주유소 개수
    now = p # 최대 갈 수 있는 곳
    j = 0 # 주유소 인덱스
    
    while now < l: # 도착지까지 도착할 수 있을때까지 반복
        while j<n and infos[j][0] <= now:
            heapq.heappush(q, -infos[j][1])
            j += 1
        # 갈 주유소가 없는 상황
        if not q:
            print(-1)
            return
        # 가장 연료 많이 주는 곳 추가
        now += -heapq.heappop(q)
        answer += 1
    print(answer)
solution()