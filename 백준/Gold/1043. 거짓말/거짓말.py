import sys
input = sys.stdin.readline
def solution():
    # 진실을 아는 사람과 연결되지 않은 파티들만 거짓말 가능
    # 진실을 아는 사람들 연결 -> Union Find 문제!!
    n, m = map(int, input().split()) # 사람 수, 파티 수
    knows = list(map(int, input().split()))
    if knows[0] == 0:
        print(m)
        return
    else:
        knows = set(knows[1:])
    parents = list(range(n+1)) # 1based index니까
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        pa = find(a)
        pb = find(b)
        if pa < pb:
            parents[pb] = pa
        else:
            parents[pa] = pb
            
    parties = []
    for _ in range(m):
        ppl = list(map(int, input().split()))[1:]
        parties.append(ppl)
        # 같은 파티 사람들은 모두 연결
        for i in range(len(ppl)-1):
            union(ppl[i], ppl[i+1])

    # 각각의 부모들 업데이트
    for i in range(1,n+1):
        parents[i] = find(i)
    # print(parents)
    new_knows = []
    for i in knows:
        new_knows.append(find(i))
    # print(parents)
    cnt = 0
    for party in parties:
        for p in party:
            if parents[p] in new_knows:
                break
        else:
            cnt += 1
    print(cnt)
solution()