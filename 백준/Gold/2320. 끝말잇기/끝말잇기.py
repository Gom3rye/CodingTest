import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]

# 각 단어의 시작 문자, 끝 문자, 길이
start = [w[0] for w in words]
end = [w[-1] for w in words]
length = [len(w) for w in words]

# 메모이제이션 딕셔너리
# key: (frozenset(used_words), last_index)
memo = {}

def dfs(used_set, last):
    key = (frozenset(used_set), last)
    if key in memo:
        return memo[key]

    best = 0
    for nxt in range(N):
        if nxt in used_set:
            continue
        if end[last] == start[nxt]:
            used_set.add(nxt)
            best = max(best, length[nxt] + dfs(used_set, nxt))
            used_set.remove(nxt)

    memo[key] = best
    return best


answer = 0
for i in range(N):
    answer = max(answer, length[i] + dfs({i}, i))

print(answer)