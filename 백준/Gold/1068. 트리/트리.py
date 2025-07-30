import sys
sys.setrecursionlimit(1000)  # 재귀 깊이 대비

def solution():
    N = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    delete = int(sys.stdin.readline())

    # 자식 리스트 만들기
    tree = [[] for _ in range(N)]
    root = -1
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)

    # 삭제된 루트 처리: 전체 삭제
    if delete == root:
        print(0)
        return

    leaf_count = 0

    def dfs(node):
        nonlocal leaf_count
        if node == delete:
            return  # 삭제 노드는 무시

        # 삭제된 자식을 제외한 실제 자식들
        children = [child for child in tree[node] if child != delete]
        if not children:
            leaf_count += 1
            return
        for child in children:
            dfs(child)

    dfs(root)
    print(leaf_count)
solution()