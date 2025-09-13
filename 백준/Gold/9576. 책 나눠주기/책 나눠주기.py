import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split()) # n개의 책, m명에게 나눠줌
        cnt = 0 # 책을 준 학생 수
        infos = list(tuple(map(int, input().split())) for _ in range(m))
        # 최대한 많은 학생들에게 책을 주기 위해 범위가 좁은 것부터 해결
        infos.sort(key=lambda x: x[1])
        visited = [False]*(n+1)
        for a, b in infos:
            for i in range(a, b+1):
                if not visited[i]:
                    visited[i] = True
                    cnt += 1
                    break
        print(cnt)
        
solution()