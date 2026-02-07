import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, k, m = map(int, input().split())

dict = defaultdict(list)
adj = [[] for _ in range(n + m + 1)]
for t in range(1, m+1):
  tube = list(map(int, input().split()))
  tube_node = n + t
  for s in tube:
    adj[s].append(tube_node)
    adj[tube_node].append(s)
    
q = deque()
visited = [-1]*(n+m+1)
q.append(1)
visited[1] = 1

ans = -1

while q:
  v= q.popleft()
  if v == n:
    ans = visited[v]
    break
  for nv in adj[v]:
    if visited[nv] == -1:
        if nv > n:
          visited[nv] = visited[v]
        else:
          visited[nv] = visited[v] + 1
        q.append(nv)
  
print(ans)