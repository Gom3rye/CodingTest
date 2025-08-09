import sys
# 재귀 깊이 제한을 늘려주어 Union-Find가 깊어져도 오류가 나지 않도록 한다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    # MST 문제 - Union Find
    # 특정 원소가 속한 집합의 루트 노드를 찾기 (경로 압축 최적화 포함)
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        edges = []
        total_cost = 0
        for _ in range(n):
            x, y, z = map(int, input().split())
            edges.append((z, x, y)) # z(비용)을 기준으로 정렬하기 위해 맨 앞에
            total_cost += z
        # 모든 길을 비용으로 오름차순 정렬
        edges.sort()
        # Union-Find를 위한 부모 테이블 초기화
        parent = list(range(m))
        mst_cost = 0
        # 가장 비용이 적은 길부터 확인하며 사이클을 만들지 않는 길 선택
        for dist, x, y, in edges:
            # 두 집이 아직 연결되어 있지 않다면 (사이클을 만들지 않는다면)
            if find_parent(parent, x) != find_parent(parent, y):
                # 두 집을 연결
                union_parent(parent, x, y)
                mst_cost += dist
        # 결과 출력
        print(total_cost-mst_cost)
solution()