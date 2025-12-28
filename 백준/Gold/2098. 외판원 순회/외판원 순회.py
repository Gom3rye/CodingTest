import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=16
    w = [list(map(int, input().split())) for _ in range(n)]
    # dp[mask][i]: mask에 해당하는 도시들을 방문했고, 현재 도시가 i일때 최소 비용
    INF = float('inf')
    dp = [[INF]*n for _ in range(1<<n)]
    dp[1][0] = 0 # 시작은 0번 도시
    # 사이클은 시작도시가 상관없다.
    for mask in range(1<<n):
        for now in range(n): # 현재 도시
            if dp[mask][now] == INF:
                continue
            # 현재 mask 상태에 city를 방문하지 않았다면 패쓰
            if not (mask & 1<<now):
                continue
            # 다음 도시 탐색
            for nxt in range(n):
                if w[now][nxt] == 0:
                    continue
                # 다음 도시 탐색 안했을 때만
                if not(mask & 1<<nxt):
                    new_mask = mask | 1<<nxt
                    dp[new_mask][nxt] = min(dp[new_mask][nxt], dp[mask][now]+w[now][nxt])
    
    # 1번 도시에서 n-1도시까지 첫 출발 도시인 0번 도시로 돌아오는 비용 더해주기
    answer = INF
    for city in range(1, n):
        if w[city][0] != 0: # city->0으로 갈 수 없는 경우는 빼고
            answer = min(answer, dp[-1][city]+w[city][0])
    print(answer)
solution()
