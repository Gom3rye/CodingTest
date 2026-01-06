import sys
import heapq
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    
    classes = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        arr.sort()
        classes.append(arr)
    
    heap = []
    current_max = 0
    
    # 초기: 각 반의 첫 원소
    for i in range(N):
        val = classes[i][0]
        heapq.heappush(heap, (val, i, 0))  # (능력치, 반 번호, 인덱스)
        current_max = max(current_max, val)
    
    ans = float('inf')
    
    while True:
        min_val, cls, idx = heapq.heappop(heap)
        ans = min(ans, current_max - min_val)
        
        # 해당 반에서 다음 학생 선택
        if idx + 1 == M:
            break  # 이 반에서 더 이상 선택 불가 → 종료
        
        next_val = classes[cls][idx + 1]
        heapq.heappush(heap, (next_val, cls, idx + 1))
        current_max = max(current_max, next_val)
    
    print(ans)

solution()
