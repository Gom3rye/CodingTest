import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

for i in range(n+1):
	graph[i].sort()

def dfs(graph, v, visited):
	visited[v] = True # 첫 노드를 방문 처리 해주고
	print(v, end=' ') # 방문했으니 출력하고

	for i in graph[v]: # 인접 노드 순회하면서
		if not visited[i]:  # 방문하지 않았다면
			dfs(graph, i, visited)  # 다시 스택에 넣기 (재귀적 호출)
		
def bfs(graph, v, visited):
	visited[v] = True  # 첫 노드 방문 처리 해주고
	q = deque([v])     # 방문한 노드 큐에 담아서 초기화

	while q:
		v = q.popleft()    # 큐에서 다시 빼고
		print(v, end=' ')  # 큐에서 뺐으니 출력하고
		for i in graph[v]:  # 인접 노드 순회하면서
			if not visited[i]: # 방문하지 않은 노드가 있다면
				visited[i] = True # 방문 처리 해주고 
				q.append(i)
	
visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)