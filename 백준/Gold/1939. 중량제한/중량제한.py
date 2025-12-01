import sys
input = sys.stdin.readline
def solution():
    # 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하기
    n, m = map(int, input().split()) # 섬<=10000 다리<=100,000
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split()) # c<=1,000,000,000
        edges.append((c, a, b))
    edges.sort(reverse=True) # Max-min이니까 내림차순 정렬
    start, end = map(int, input().split()) # 공장 시작, 끝
    parents = list(range(n+1))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parents[b] = a
        else:
            parents[a] = b

    # 목표: start와 end가 언제 연결되느냐만 중요
    for cost, a, b in edges:
        if find(a) != find(b): # 사이클 방지 & 불필요한 union 호출 줄여서 성능 향상
            union(a, b) # 이미 같은 집합이면 아무 변화 없고(parents 갱신 안됨), 달라야만 집합이 합쳐진다.
            # 두 공장이 연결되는 순간 멈추기
            if find(start) == find(end):
                print(cost)
                break  
solution()