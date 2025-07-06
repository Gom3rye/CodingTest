import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())

    MAX_POS = 100001 # 문제에서 N, K의 최대값이 100,000이므로 배열 크기는 100,001로 설정
    
    # 각 위치까지의 최소 시간을 저장하는 배열
    # -1은 아직 방문하지 않았음을 의미
    dist = [-1] * MAX_POS 
    
    # 각 위치까지의 최단 경로의 수를 저장하는 배열
    ways = [0] * MAX_POS

    q = deque()

    # 시작 위치 초기화
    dist[n] = 0
    ways[n] = 1
    q.append(n)

    min_time = -1 # K에 도달하는 최소 시간
    
    while q:
        now = q.popleft()
        if min_time != -1 and dist[now] > min_time:
            continue

        # 현재 위치에서 이동 가능한 다음 위치들
        # now*2, now-1, now+1 순서는 결과에 영향을 주지 않지만, BFS의 특성상 순서대로 탐색
        next_positions = [now * 2, now - 1, now + 1]

        for next_pos in next_positions:
            # 유효한 범위 내에 있는지 확인
            if 0 <= next_pos < MAX_POS:
                # 1. next_pos를 처음 방문하는 경우 (최단 경로 발견)
                if dist[next_pos] == -1:
                    dist[next_pos] = dist[now] + 1
                    ways[next_pos] = ways[now] # 현재까지의 경로 수를 그대로 가져옴
                    q.append(next_pos)
                    
                    # 만약 K에 도달했다면, 최소 시간을 기록
                    if next_pos == k:
                        if min_time == -1: # K에 처음 도달한 경우
                            min_time = dist[next_pos]

                # 2. next_pos를 이미 방문했지만, 현재 경로가 최단 경로와 같은 길이인 경우
                #    (K에 도달하는 다른 최단 경로를 찾은 경우)
                elif dist[next_pos] == dist[now] + 1:
                    ways[next_pos] += ways[now] # 경로 수 누적
                    
    print(dist[k])
    print(ways[k])

solution()