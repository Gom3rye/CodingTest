import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #도시 <=200
    m = int(input()) # #여행계획에 속한 도시 <=1000
    # 같은 도시 여러 번 방문 가능
    connected = [list(map(int, input().split())) for _ in range(n)]
    plan = list(map(int, input().split())) # 여행계획
    # 연결 여부 묻기: union-find
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
    
    for i in range(n):
        for j in range(i+1, n): # 양방향이니까
            if connected[i][j] == 1:
                union(i, j)
    # 조상 갱신
    for i in range(n):
        find(i)

    answer = parents[plan[0]-1] # 0based index
    for city in plan[1:]:
        city -= 1 # 0based index
        if parents[city] != answer:
            print("NO")
            return
    else:
        print("YES")

solution()