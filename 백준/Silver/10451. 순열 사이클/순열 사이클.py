import sys
input = sys.stdin.readline
from collections import deque

def solution():
    T = int(input())  # 테스트 케이스 개수
    for _ in range(T):
        n = int(input())  # 학생 수
        arr = [0] + list(map(int, input().split()))  # 각 학생이 선택한 사람 (1-based indexing)
        visited = [False] * (n+1)
        result = 0  # 팀

        def bfs(x):
            visited[x] = True
            q = deque([x])
            while q:
                now = q.popleft()
                next = arr[now]
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
        for i in range(1, n+1):
            if not visited[i]:
                bfs(i)
                result += 1
        print(result)
solution()