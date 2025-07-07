import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, k = map(int, input().split())
    MAX = 100001
    dist = [-1]*MAX
    ways = [0]*MAX
    def bfs():
        q = deque([n])
        dist[n] = 0
        ways[n] = 1
        while q:
            now = q.popleft()
            for next in [now*2, now-1, now+1]:
                if 0<=next<MAX:
                    if dist[next] == -1:
                        dist[next] = dist[now]+1
                        ways[next] = ways[now] # 현재까지의 경로 수를 그대로 가져옴
                        q.append(next)
                    elif dist[next] == dist[now]+1: # 이미 한 번 방문한 경우
                        ways[next] += ways[now]
    bfs()
    print(dist[k])
    print(ways[k])

solution()