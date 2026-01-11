import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 정점의 수 <=10,000
    weight = [0]+list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    # 우수마을과 비슷
    dp = [[0]*2 for _ in range(n+1)] # dp[i][0]:i를 선택하지 않았을 때 최대값, dp[i][1]:i를 선택했을때 최대값
    visited = [False]*(n+1) # 트리는 무방향 그래프니까 갔던 데 또 가지 않기 위해서
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    def dfs(now):
        visited[now] = True
        # now에 관해 dp 초기화
        dp[now][1] = weight[now]
        for nxt in tree[now]:
            if not visited[nxt]:
                dfs(nxt)
                dp[now][0] += max(dp[nxt])
                dp[now][1] += dp[nxt][0]

    dfs(1)
    max_weight = max(dp[1])
    print(max_weight)
    answer = []
    # 이제 역추적해서 구성 요소 출력하기
    visited = [False]*(n+1)
    def trace(now, selected):
        visited[now] = True
        if selected:
            answer.append(now)
            for nxt in tree[now]:
                if not visited[nxt]:
                    trace(nxt, False) # now가 선택되었으니까 nxt는 선택하면 안된다.
        else:
            for nxt in tree[now]:
                if not visited[nxt]:
                    if dp[nxt][1] > dp[nxt][0]:
                        trace(nxt, True)
                    else:
                        trace(nxt, False)

    # 1을 고른게 더 크다면 1은 고르기
    if dp[1][1] > dp[1][0]:
        trace(1, True)
    else:
        trace(1, False)
    print(*sorted(answer))
solution()