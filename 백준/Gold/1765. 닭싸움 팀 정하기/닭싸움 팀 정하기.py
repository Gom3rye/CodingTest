import sys
input = sys.stdin.readline
def solution():
    # 만들어질 수 있는 최대 팀 구하기
    n = int(input()) # #학생 <=1000
    m = int(input()) # #인간관계 <=5000
    parents = list(range(n))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parents[b] = a
    enemies = [[] for _ in range(n)] # 0based index
    for _ in range(m):
        r, a, b = input().split()
        a, b = int(a)-1, int(b)-1 # 0based index
        if r == 'E':
            enemies[a].append(b)
            enemies[b].append(a) # 친구관계는 양방향
        else: # r == 'F'
            union(a, b)

    # 적의 적은 친구다
    for i in range(n):
        ne = len(enemies[i])
        if ne >= 2:
            for j in range(ne-1):
                union(enemies[i][j], enemies[i][j+1])

    for i in range(n):
        find(i)
    
    parents_set = set(parents)
    print(len(parents_set))
solution()