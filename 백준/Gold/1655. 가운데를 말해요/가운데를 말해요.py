import sys, heapq
input = sys.stdin.readline
def solution():
    n = int(input())
    max_heap = [] # 중간값 이하 숫자 저장 (왼쪽, 가장 큰 값을 유지 (중간값 후보))
    min_heap = [] # 중간값 초과 (오른쪽, 중간값 초과 값들)
    result = []
    for _ in range(n):
        num = int(input())
        # 1. max_heap에 일단 넣음 (음수로 넣어서 최대힙처럼 사용)
        heapq.heappush(max_heap, -num)
        
        # 2. max_heap의 최대값을 min_heap에 넣음 → 항상 max가 왼쪽에
        heapq.heappush(min_heap, -heapq.heappop(max_heap)) # 왼쪽 최대값을 오른쪽 최소힙으로 이동
        
        # 3. 왼쪽 길이가 작아졌다면 → 균형 맞추기
        if len(max_heap) < len(min_heap): # 항상 max_heap의 길이 ≥ min_heap의 길이가 되도록 유지
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        # 4. max_heap의 top이 중간값
        result.append(-max_heap[0])

        # print(f"max heap: {max_heap}")
        # print(f"min_heal: {min_heap}")
    print("\n".join(map(str, result)))
solution()