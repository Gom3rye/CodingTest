import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution(n, wires):
    answer = 10**9
    # 트리 만들어주기
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    visited[1] = True
    def dfs(start):
        nonlocal answer
        size = 1 # 자기자신
        for nxt in graph[start]:
            if not visited[nxt]:
                visited[nxt] = True
                subtree = dfs(nxt) # nxt를 루트로 가지고 있는 subtree의 size
                # diff값으로 answer 계산
                answer = min(answer, abs(n-2*subtree))
                size += subtree
        return size
    dfs(1)
    return answer