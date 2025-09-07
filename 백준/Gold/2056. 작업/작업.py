from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    
    time = [0] * (N + 1)              # 작업 시간
    in_degree = [0] * (N + 1)         # 선행 작업 수
    graph = [[] for _ in range(N + 1)] # 인접 리스트 (후속 작업들)

    for i in range(1, N + 1):
        data = list(map(int, input().split()))
        time[i] = data[0]
        in_degree[i] = data[1]
        for pre in data[2:]:
            graph[pre].append(i)

    # dp[i]: i번 작업을 끝내기 위한 최소 시간
    dp = [0] * (N + 1)
    queue = deque()

    # 선행 작업이 없는 작업부터 시작
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            dp[i] = time[i]
            queue.append(i)

    while queue:
        curr = queue.popleft()
        for next_task in graph[curr]:
            in_degree[next_task] -= 1
            dp[next_task] = max(dp[next_task], dp[curr] + time[next_task])
            if in_degree[next_task] == 0:
                queue.append(next_task)

    print(max(dp))

solution()
