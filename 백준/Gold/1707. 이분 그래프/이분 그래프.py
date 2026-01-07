import sys
from collections import deque
from math import log2
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        v, e = map(int, input().split()) #<=20000, 200,000
        graph = [[] for _ in range(v+1)]
        for _ in range(e):
            a, b = map(int, input().split())
            # 사이클이 생기면 안됨
            graph[a].append(b)
            graph[b].append(a)
        color = [0]*(v+1) # 노드마다 색칠하기
        # 노드마다 bfs로 탐색하며 색칠하고 이분 그래프인지 확인하기
        def bfs(now):
            q = deque([now])
            color[now] = 1
            while q:
                now = q.popleft()
                for nxt in graph[now]:
                    if color[nxt] == 0:
                        color[nxt] = -color[now] # 반전
                        q.append(nxt)
                    elif color[nxt] == color[now]:
                        return False
            return True

        for i in range(1, v+1):
            if color[i] == 0:
                answer = bfs(i)
                if not answer:
                    print("NO")
                    break
        else:
            print("YES")
            
solution()