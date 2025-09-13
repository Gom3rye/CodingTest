import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    def find(x):
        if x >= n or parent[x] == x:
            return parent[x]
        parent[x] = find(parent[x])
        return parent[x]

    for _ in range(t):
        n, m = map(int, input().split()) # n개의 책, m명에게 나눠줌
        parent = list(range(n+1)) # 각 책의 대표 부모 초기화
        cnt = 0 # 책을 준 학생 수
        infos = list(tuple(map(int, input().split())) for _ in range(m))
        # 최대한 많은 학생들에게 책을 주기 위해 범위가 좁은 것부터 해결
        infos.sort(key=lambda x: x[1])
        for a, b in infos:
            aparent = find(a) # a부터 가능한 가장 작은 책 번호 찾기
            if aparent <= b:
                parent[aparent] += 1 # aparent책은 사용됐으므로 다음 책으로 대표 부모를 옮김
                cnt += 1
        print(cnt)
solution()