def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# 입력
N, M = map(int, input().split())
data = list(map(int, input().split()))
truth_count = data[0]
truth_people = data[1:]

parties = []
parent = [i for i in range(N+1)]

# 파티 정보 입력 및 유니온 처리
for _ in range(M):
    arr = list(map(int, input().split()))
    people = arr[1:]
    parties.append(people)
    # 같은 파티 사람들은 모두 연결
    for i in range(len(people) - 1):
        union(people[i], people[i+1])

# 진실을 아는 집합의 대표자들
truth_roots = set(find(p) for p in truth_people)

# 각 파티마다 검사
ans = 0
for party in parties:
    # 진실 집합과 연결된 사람 있는지 확인
    if any(find(p) in truth_roots for p in party):
        continue  # 진실 말해야 함
    ans += 1  # 거짓말 가능

print(ans)
