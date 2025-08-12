from collections import deque

def bfs(N, K):
    MAX = 100001
    visited = [-1] * MAX
    q = deque()
    q.append(N)
    visited[N] = 0  # 시작 위치의 시간은 0

    while q:
        current = q.popleft()

        if current == K:
            return visited[current]  # 목적지 도달 시 시간 반환

        # 순간이동 (0초): 우선 처리 → deque의 앞에 추가
        teleport = current * 2
        if 0 <= teleport < MAX and visited[teleport] == -1:
            visited[teleport] = visited[current]
            q.appendleft(teleport)

        # 걷기 (1초): 뒤에 추가
        for next_pos in [current-1, current+1]:
            if 0 <= next_pos < MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                q.append(next_pos)

# 입력 처리
N, K = map(int, input().split())
print(bfs(N, K))