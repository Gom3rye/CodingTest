import sys
input = sys.stdin.readline
def solution():
    k, n, f = map(int, input().split()) # #소풍갈 학생 <=62, #학생 <=900, #친구관계 <=5600
    # 평균 차수 계산: 2*간선//정점 -> 여기선 12.44정도로 작음, 백트레킹에서는 평균 차수가 분기 수를 결정하기 때문에 백트레킹 가능
    friend = [[] for _ in range(n+1)]
    degree = [0]*(n+1)
    for _ in range(f):
        a, b = map(int, input().split())
        friend[a].append(b)
        friend[b].append(a) # 양방향
        degree[a] += 1 # 차수가 k-1개보다 작으면 소풍갈 학생이 될 수 없다.
        degree[b] += 1

    def is_valid(nxt):
        for mem in picnic:
            if not nxt in friend[mem]:
                return False
        return True

    picnic = []
    def backtracking(now):
        if len(picnic) == k:
            print(*picnic, sep='\n')
            sys.exit()

        for nxt in range(now+1, n+1):
            if degree[nxt] < k-1:
                continue
            if is_valid(nxt):
                picnic.append(nxt)
                backtracking(nxt)
                picnic.pop()
                        
    # backtracking으로 소풍갈 친구들의 "조합" 구하기!
    backtracking(0)
    print(-1)
solution()