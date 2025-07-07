import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dist(a, b):
    return sum(x != y for x, y in zip(a, b))

def solution(begin, target, words):
    if target not in words:
        return 0

    min_count = int(1e9)
    visited = [False] * len(words)

    def dfs(current, level):
        nonlocal min_count
        if current == target:
            min_count = min(min_count, level)
            return 

        for i, word in enumerate(words):
            if not visited[i] and dist(current, word) == 1:
                visited[i] = True
                dfs(word, level+1)
                visited[i] = False  # 백트래킹
                
    dfs(begin, 0)
    return min_count
