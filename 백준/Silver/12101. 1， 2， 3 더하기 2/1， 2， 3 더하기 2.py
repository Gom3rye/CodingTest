import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    result = []
    count = [0]  # 리스트로 감싸서 참조 가능하게 함
    found = [False]

    def dfs(total, path):
        if found[0]:
            return
        if total == n:
            count[0] += 1
            if count[0] == k:
                print('+'.join(map(str, path)))
                found[0] = True
            return
        for i in [1, 2, 3]:  # 사전순: 1 → 2 → 3
            if total + i <= n:
                dfs(total + i, path + [i])

    dfs(0, [])
    if not found[0]:
        print(-1)

solution()