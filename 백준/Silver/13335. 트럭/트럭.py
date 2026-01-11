import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, w, L =  map(int, input().split()) # #트럭 <=1000, 다리길이 <=100, 최대하중 <=1000
    trucks = deque(map(int, input().split())) # 트럭의 무게
    # 모든 트럭이 다리를 건너는 최단시간 구하기
    # 다리 자체를 움직이는 컨베이어 벨트라고 생각하고 고정된 길이의 deque로 만들기=> 복잡한 위치 계산 없이 단순 pop, push문제로 바꿀 수 있다.
    bridge = deque([0]*w) # w길이만큼
    # 사이클 로직:
    # 1. 있던 트럭 나가기
    # 2. 새 트럭 들어오기
    # 3. 시간 흐르기
    now_weight = 0
    time = 0
    while bridge: # 다리 길이는 트럭이 머무르는 시간과 같다!
        # 나가기
        out = bridge.popleft()
        now_weight -= out

        # 들어오기
        if trucks:
            # 들어올 수 있다면 다리에 넣고
            if now_weight+trucks[0] <= L:
                new = trucks.popleft()
                bridge.append(new)
                now_weight += new
            else: # 들어올 수 없다면 
                bridge.append(0) # 빈공간 채워서 트럭 전진시킴
        
        time += 1
    print(time)
solution()