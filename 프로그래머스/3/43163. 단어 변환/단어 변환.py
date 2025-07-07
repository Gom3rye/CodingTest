def dist(a, b):
    return sum(x != y for x, y in zip(a, b))

def solution(begin, target, words):
    if target not in words:
        return 0

    min_count = [float('inf')]
    visited = [False] * len(words)

    def dfs(current, depth):
        if current == target:
            min_count[0] = min(min_count[0], depth)
            return

        for i, word in enumerate(words):
            if not visited[i] and dist(current, word) == 1:
                visited[i] = True
                dfs(word, depth + 1)
                visited[i] = False  # 백트래킹

    dfs(begin, 0)
    return min_count[0] if min_count[0] != float('inf') else 0
