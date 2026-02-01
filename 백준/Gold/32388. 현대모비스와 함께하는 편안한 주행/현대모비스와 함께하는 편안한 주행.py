import sys
import math
import heapq

input = sys.stdin.readline

def solve():
    # 1. 입력 처리
    try:
        line1 = input().split()
        if not line1: return
        a, b = map(int, line1)
        
        line2 = input().split()
        if not line2: return
        n = int(line2[0])
    except:
        return
    
    signs = []
    for _ in range(n):
        signs.append(tuple(map(int, input().split())))
    
    start_node = 0
    end_node = n + 1
    total_nodes = n + 2
    nodes = [(0, 0)] + signs + [(a, b)]
    
    # 2. 다익스트라
    distances = [float('inf')] * total_nodes
    distances[start_node] = 0
    pq = [(0.0, start_node)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if curr_dist > distances[curr_node]:
            continue
            
        if curr_node == end_node:
            break
            
        curr_pos = nodes[curr_node]
        for next_node in range(total_nodes):
            if curr_node == next_node: continue
            
            next_pos = nodes[next_node]
            # math.isqrt나 정수 연산이 불가능하므로 hypot을 사용하되 
            # 최대한 정밀도를 유지합니다.
            d = math.hypot(curr_pos[0] - next_pos[0], curr_pos[1] - next_pos[1])
            
            # 가중치 결정 규칙
            if (curr_node == 0 and next_node == n + 1) or (curr_node == n + 1 and next_node == 0):
                weight = d
            elif curr_node == 0 or curr_node == n + 1 or next_node == 0 or next_node == n + 1:
                weight = max(0.0, d - 1.0)
            else:
                weight = max(0.0, d - 2.0)
            
            if distances[next_node] > curr_dist + weight:
                distances[next_node] = curr_dist + weight
                heapq.heappush(pq, (distances[next_node], next_node))
                
    ans = distances[end_node]
    
    # 3. 💡 출력 정밀도 보정
    # 만약 정답이 0에 수렴하면 0 출력
    if ans < 1e-11:
        print(0)
    else:
        # 소수점 10번째 자리에서 반올림하여 9번째 자리까지 출력
        # 예제 1에서 2.236067978을 요구한다면 반올림이 핵심입니다.
        result = "{:.9f}".format(ans)
        # 불필요한 뒷자리 0을 제거하되, 예제 출력 형식을 최대한 따릅니다.
        if "." in result:
            result = result.rstrip('0').rstrip('.')
        print(result)

if __name__ == "__main__":
    solve()