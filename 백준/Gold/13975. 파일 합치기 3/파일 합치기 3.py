import sys
import heapq
input = sys.stdin.readline

def solution():
    T = int(input())
    
    for _ in range(T):
        K = int(input())
        files = list(map(int, input().split()))
        
        heapq.heapify(files)
        
        total_cost = 0
        
        while len(files) > 1:
            a = heapq.heappop(files)
            b = heapq.heappop(files)
            cost = a + b
            total_cost += cost
            heapq.heappush(files, cost)
        
        print(total_cost)

solution()
