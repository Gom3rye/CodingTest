import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def solution():
    n = int(input()) # #섬 <=123456
    tree = [[] for _ in range(n+1)]
    # 자식->부모->루트(1)로만 가는 트리, 1늑대는 1양만 먹을 수 있으므로 모든 자식들은 다 계산이 되어서 부모노드로 가야 한다.
    # 현재 노드의 상태가 자식 하나하나에 독립적으로 영향을 받는다 -> for문 안에 조작문(우수마을)
    # 현재 노드의 상태가 자식들을 전부 모은 결과에 한 번만 영향을 받는다 -> for문 밖에 조작문(양구출작전)
    node = [None]*(n+1) # node[1]: 1의 (양/늑대, 수) 
    for i in range(2, n+1):
        animal, cnt, bridge = input().split()
        tree[int(bridge)].append(i) # tree[nxt] = now
        node[i] = (animal, int(cnt))

    def dfs(now):
        sheep = 0
        for nxt in tree[now]:
            sheep += dfs(nxt)
        
        if now != 1: # node에 관한 정보는 2노드부터
            animal, cnt = node[now]
            if animal == 'S':
                sheep += cnt
            else:
                sheep = max(sheep-cnt, 0)
        return sheep
    print(dfs(1))
solution()