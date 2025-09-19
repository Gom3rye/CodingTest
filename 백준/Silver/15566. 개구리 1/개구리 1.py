import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 개구리의 흥미도: frogs[i] = [음식, 취미, 가족, 철학]
frogs = [list(map(int, input().split())) for _ in range(N)]

# 개구리의 선호 연꽃
preferred = [[] for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    preferred[i] = [a - 1] if a == b else [a - 1, b - 1]

# 통나무 정보: (flower1, flower2, topic)
logs = []
for _ in range(M):
    a, b, t = map(int, input().split())
    logs.append((a - 1, b - 1, t - 1))  # 주제는 0-indexed

# 연꽃마다 배치된 개구리 번호 (인덱스: 연꽃 번호)
placement = [-1] * N
used = [False] * N  # 개구리 중복 배치 방지

def is_valid():
    for f1, f2, topic in logs:
        g1 = placement[f1]
        g2 = placement[f2]
        if g1 == -1 or g2 == -1:
            continue
        if frogs[g1][topic] != frogs[g2][topic]:
            return False
    return True

def dfs(frog_index):
    if frog_index == N:
        if is_valid():
            print("YES")
            # frog[flower] = 개구리 -> 우리는 placement[flower] = 개구리니까 맞음
            print(' '.join(str(p + 1) for p in placement))
            sys.exit(0)
        return

    for flower in preferred[frog_index]:
        if placement[flower] != -1:
            continue
        placement[flower] = frog_index
        used[frog_index] = True
        dfs(frog_index + 1)
        placement[flower] = -1
        used[frog_index] = False

dfs(0)
print("NO")
