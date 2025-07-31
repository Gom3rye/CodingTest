import sys
from collections import deque

# 빠른 입력을 위한 설정
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    
    # B -> A 단방향 그래프
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    counts = [0] * (n + 1)
    max_count = 0

    # 1번부터 N번까지 모든 컴퓨터를 시작점으로 하여 탐색
    for i in range(1, n + 1):
        # 재귀가 아닌 스택을 이용한 DFS
        stack = [i]
        visited = [False] * (n + 1)
        visited[i] = True
        count = 0
        
        while stack:
            current_com = stack.pop()
            count += 1
            
            for neighbor in graph[current_com]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        
        # 각 시작점별 해킹 수를 저장하고, 실시간으로 최댓값을 갱신
        counts[i] = count
        if count > max_count:
            max_count = count
    
    # 결과 출력
    result = []
    for i in range(1, n + 1):
        if counts[i] == max_count:
            result.append(i)
    
    print(*result)

solution()