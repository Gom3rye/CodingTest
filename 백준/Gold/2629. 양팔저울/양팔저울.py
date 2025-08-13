import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    weights = list(map(int, input().split()))
    m = int(input())
    marbles = list(map(int, input().split()))

    possible = set()

    def dfs(i, weight):
        if (i, weight) in visited:
            return
        visited.add((i, weight))
        if i == n:
            possible.add(abs(weight))
            return
        # 왼쪽에 추가 올리기 (무게 증가)
        dfs(i + 1, weight + weights[i])
        # 오른쪽에 추가 올리기 (무게 감소)
        dfs(i + 1, weight - weights[i])
        # 사용 안 함
        dfs(i + 1, weight)

    visited = set()
    dfs(0, 0)

    result = []
    for marble in marbles:
        result.append("Y" if marble in possible else "N")
    print(" ".join(result))

solution()
