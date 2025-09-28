import sys
from collections import deque

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# --- 입력 처리 ---
N = int(input())
# N이 1일 경우, 점프 없이 도착한 것이므로 0을 출력하고 종료
if N == 1:
    print(0)
    sys.exit()

maze = list(map(int, input().split()))

# --- BFS 설정 ---
# visited[i]: i번 칸까지 도달하는 데 필요한 최소 점프 횟수
# 방문하지 않은 칸은 -1로 초기화
visited = [-1] * N
q = deque()

# 시작점 설정: 0번 칸에서 0번의 점프로 시작
q.append(0)
visited[0] = 0

# --- BFS 탐색 ---
while q:
    current_pos = q.popleft()
    max_jump = maze[current_pos]
    
    # 현재 위치에서 가능한 모든 점프를 시도
    for jump in range(1, max_jump + 1):
        next_pos = current_pos + jump
        
        # 미로 범위를 벗어나면 중단
        if next_pos >= N:
            continue
            
        # 아직 방문하지 않은 칸이라면 방문 처리 후 큐에 추가
        if visited[next_pos] == -1:
            visited[next_pos] = visited[current_pos] + 1
            q.append(next_pos)

# --- 결과 출력 ---
# 마지막 칸의 visited 값을 출력 (도달하지 못했다면 초기값 -1이 그대로 출력됨)
print(visited[N - 1])