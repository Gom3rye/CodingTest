from collections import deque

def solution():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    visited = [False] * N
    queue = deque()
    queue.append(0)
    visited[0] = True

    while queue:
        cur = queue.popleft()

        # 마지막 돌에 도달하면 성공
        if cur == N - 1:
            print("YES")
            return

        for nxt in range(cur + 1, N):
            cost = (nxt - cur) * (1 + abs(A[cur] - A[nxt]))
            if cost <= K and not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    # 끝까지 도달 못했으면 실패
    print("NO")

solution()
