import sys, heapq
input = sys.stdin.readline
def solve():
    # 테스트 케이스 개수
    t = int(input())
    for _ in range(t):
        m = int(input())
        nums = []
        # 한 줄에 10개씩 들어오는 입력 처리
        while len(nums) < m:
            nums.extend(map(int, input().split()))
        
        max_heap = [] # 중앙값 이하 (최대 힙)
        min_heap = [] # 중앙값 초과 (최소 힙)
        medians = []
        
        for i in range(m):
            val = nums[i]
            
            # 1. 일단 번갈아가며 힙에 추가
            if len(max_heap) == len(min_heap):
                heapq.heappush(max_heap, -val)
            else:
                heapq.heappush(min_heap, val)
            
            # 2. 최대 힙의 루트가 최소 힙의 루트보다 크면 스왑
            if min_heap and -max_heap[0] > min_heap[0]:
                max_val = -heapq.heappop(max_heap)
                min_val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -min_val)
                heapq.heappush(min_heap, max_val)
            
            # 3. 홀수 번째마다 중앙값 기록
            if (i + 1) % 2 == 1:
                medians.append(-max_heap[0])
        
        # 출력 양식에 맞춰 출력
        print(len(medians))
        for i in range(len(medians)):
            print(medians[i], end=' ')
            if (i + 1) % 10 == 0: # 10개마다 줄바꿈
                print()
        if len(medians) % 10 != 0:
            print()

solve()