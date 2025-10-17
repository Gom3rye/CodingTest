import sys; input = sys.stdin.readline
N, M = map(int, input().split())
wok = list(map(int, input().split()))
wok_set = set(wok)
for i in range(M):
    for j in range(i + 1, M):
        wok_set.add(wok[i] + wok[j])
INF = 1234567890
memo = [INF for _ in range(10001)]
memo[0] = 0
for i in range(N):
    for k in wok_set:
        if i + k > 10000: continue
        memo[i + k] = min(memo[i] + 1, memo[i + k])

if INF == memo[N]:
    print(-1)
else:
    print(memo[N])