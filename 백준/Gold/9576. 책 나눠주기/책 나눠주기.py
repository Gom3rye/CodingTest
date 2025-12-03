import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split()) # 책번호 <=1000, 인원수 <=1000
        infos = [list(map(int, input().split())) for _ in range(m)]
        # 최대한 많은 학생들을 주기 위해 upper limit이 가장 적은 순으로 나열
        infos.sort(key=lambda x: x[1])
        parents = list(range(n+2)) # 관리해야 할 노드만큼 만들기
        def find(x): # x이하의 사용가능한 가장 작은 책 찾기
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        cnt = 0
        for a, b in infos:
            assign = find(a)
            if assign > b : # 요청한 구간보다 큰 책은 할당할 수 없음
                continue
            cnt += 1
            parents[assign] += 1
        print(cnt)
solution()
