import sys
input = sys.stdin.readline
write = sys.stdout.write

n, k = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]

# 전후 관계 입력
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = True

# 플로이드-워셜 알고리즘 (경로 유무만 확인)
def floyd():
    for mid in range(1, n + 1):
        g_mid = graph[mid]
        for start in range(1, n + 1):
            if not graph[start][mid]:
                continue
            g_start = graph[start]
            for end in range(1, n + 1):
                if g_mid[end]:
                    g_start[end] = True

# 쿼리 처리
s = int(input())
results = []
floyd()
for _ in range(s):
    a, b = map(int, input().split())
    if graph[a][b]:
        results.append("-1\n")
    elif graph[b][a]:
        results.append("1\n")
    else:
        results.append("0\n")

write(''.join(results))
