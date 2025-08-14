import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, k = map(int, input().split())
    well = list(map(int, input().split()))
    info = []
    for w in well:
        info.append((w, 0))
    q = deque(info)
    visited = set(well)
    total_dist = 0
    while q:
        now, dist = q.popleft()
        for nxt in [now+1, now-1]:
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, dist+1))
                total_dist += (dist+1)
                if len(visited) == k+len(well):
                    print(total_dist)
                    return
solution()