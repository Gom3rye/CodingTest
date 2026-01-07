import sys
from collections import deque
from math import log2
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        n = int(input()) # #노드 <=10000
        graph = [[] for _ in range(n+1)]
        for _ in range(n-1):
            a, b = map(int, input().split())
            graph[b].append(a) # b의 조상은 a
        v1, v2 = map(int, input().split()) # 공통조상을 찾아야 하는 두 노드
        def find_ancestors(child):
            parents = []
            parents_set = set()
            q = deque()
            q.append(child)
            parents.append(child)
            parents_set.add(child)
            while q:
                child = q.popleft()
                for parent in graph[child]:
                    parents.append(parent)
                    parents_set.add(parent)
                    q.append(parent)
            return parents, parents_set
        v1_parents, v1_parents_set = find_ancestors(v1)
        _, v2_parents_set = find_ancestors(v2)
        common_parents = v1_parents_set & v2_parents_set
        min_idx, answer = float('inf'), -1
        for common_ancestor in common_parents:
            idx = v1_parents.index(common_ancestor)
            if idx < min_idx:
                min_idx = idx
                answer = common_ancestor
        print(answer)
solution()