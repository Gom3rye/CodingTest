import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n, root, q = map(int, input().split()) # 정점 수 <=10^5, 루트 번호 <=n, 쿼리 수 <=10^5
    # 정점u를 루트로 하는 서브트리에 속한 정점의 수 출력
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a) # 무향 그래프 But, 루트를 기준으로 dfs 돌리면 parent<->child 관계 자동으로 정해진다.
    tree = [[] for _ in range(n+1)] # 자식 저장
    subtree_size = [1]*(n+1)
    # dfs (부모자식 구조 만들기)
    def makeTree(currentNode, parent):
        for nxt in graph[currentNode]:
            if nxt != parent:
                # add node to currentNode's child & set node's parent to currentNode
                tree[currentNode].append(nxt)
                makeTree(nxt, currentNode)
    
    makeTree(root, -1) # root를 정점으로 하는 tree 구성
    # dfs (서브트리 크기 계산)
    def countSubtreeNodes(currentNode):
        for child in tree[currentNode]:
            countSubtreeNodes(child)
            subtree_size[currentNode] += subtree_size[child]
    
    countSubtreeNodes(root)
    for _ in range(q):
        node = int(input())
        print(subtree_size[node])
solution()