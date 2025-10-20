import sys

# 재귀 깊이 제한을 늘려줍니다 (N이 5000일 경우 필요할 수 있음)
sys.setrecursionlimit(10**6)

# 빠른 입력을 위한 설정
input = sys.stdin.readline

def solve():
    """
    메모이제이션을 이용한 DFS 풀이.
    dp[i] = i번 쉼터에서 시작하는 가장 긴 경로의 길이
    """
    N, M = map(int, input().split())
    heights = [0] + list(map(int, input().split()))
    
    # 인접 리스트로 그래프 표현
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        # 높이에 따라 단방향 그래프를 만듭니다.
        if heights[u] < heights[v]:
            graph[u].append(v)
        elif heights[v] < heights[u]:
            graph[v].append(u)
            
    # DP 테이블: -1은 아직 계산되지 않았음을 의미
    dp = [-1] * (N + 1)

    def dfs(node):
        # 이미 계산된 값이 있다면 바로 반환
        if dp[node] != -1:
            return dp[node]
        
        # 기본값은 자기 자신만 방문하는 경우: 1
        max_path = 1
        
        # 현재 노드에서 갈 수 있는 더 높은 노드들을 탐색
        for neighbor in graph[node]:
            # 다음 노드에서 시작하는 경로 길이에 1을 더한 값과 현재까지의 최대 경로 길이를 비교
            max_path = max(max_path, 1 + dfs(neighbor))
        
        # 계산된 값을 저장하고 반환
        dp[node] = max_path
        return dp[node]

    # 모든 쉼터에 대해 DFS를 실행하여 DP 테이블을 채웁니다.
    for i in range(1, N + 1):
        if dp[i] == -1:
            dfs(i)
            
    # 결과 출력
    for i in range(1, N+1):
        print(dp[i])

solve()