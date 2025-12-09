import sys
input = sys.stdin.readline
def solution():
    # 친구 관계가 생길때마다 두 사람이 속한 root를 합치고, 그 root의 size를 출력하기
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parents[b] = a # a를 조상으로 만들고
            size[a] += size[b] # a의 크기에 b의 크기를 더해주기
        return size[a]
    t = int(input()) # 테스트 케이스의 개수
    for _ in range(t):
        f = int(input()) # 친구 관계의 수 <100,000
        parents = dict() # parents[f1] = f2
        size = dict() # size[root] = root가 대표하는 집합의 크기
        for _ in range(f):
            f1, f2 = input().split()
            # 새로운 사람 등로
            if f1 not in parents:
                parents[f1] = f1
                size[f1] = 1
            if f2 not in parents:  
                parents[f2] = f2
                size[f2] = 1
            print(union(f1, f2))          
                
solution()