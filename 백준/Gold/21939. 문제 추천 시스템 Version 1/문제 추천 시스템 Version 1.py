import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())
    
    min_heap = []
    max_heap = []
    alive = {}
    
    for _ in range(N):
        P, L = map(int, input().split())
        heapq.heappush(min_heap, (L, P))
        heapq.heappush(max_heap, (-L, -P))
        alive[P] = L
    
    M = int(input())
    
    for _ in range(M):
        cmd = input().split()
        
        if cmd[0] == "add":
            P, L = int(cmd[1]), int(cmd[2])
            heapq.heappush(min_heap, (L, P))
            heapq.heappush(max_heap, (-L, -P))
            alive[P] = L
        
        elif cmd[0] == "solved":
            P = int(cmd[1])
            del alive[P]
        
        else:  # recommend
            x = int(cmd[1])
            
            if x == 1:
                while True:
                    L, P = max_heap[0]
                    L, P = -L, -P
                    if P in alive and alive[P] == L:
                        print(P)
                        break
                    heapq.heappop(max_heap)
            else:
                while True:
                    L, P = min_heap[0]
                    if P in alive and alive[P] == L:
                        print(P)
                        break
                    heapq.heappop(min_heap)

solution()
