from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline
MAX = float('inf')
MAXCOST = 2501
N, M = map(int, input().split())
fuel_cost = list(map(int, input().split()))
edge_dict = defaultdict(list)
for _ in range(M) :
  a, b, c = map(int, input().split())
  edge_dict[a-1].append((b-1, c))
  edge_dict[b-1].append((a-1, c))

visited = [[MAX]*MAXCOST for _ in range(N)]
visited[0][-1] = 0
q = [(0, MAXCOST, 0)]

while q :
  tot_cost, min_cost, node = heappop(q)
  if node == N-1 :
    print(tot_cost)
    break
  min_cost = min(min_cost, fuel_cost[node])
  for nxt, nxt_dist in edge_dict[node] :
    if visited[nxt][min_cost] > tot_cost + min_cost*nxt_dist :
      visited[nxt][min_cost] = tot_cost + min_cost*nxt_dist
      heappush(q, (tot_cost + min_cost*nxt_dist, min_cost, nxt))
