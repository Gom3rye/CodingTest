import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    signs = input().strip()

    matrix = [[0] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(i, n):
            if signs[idx] == '+':
                matrix[i][j] = 1
            elif signs[idx] == '-':
                matrix[i][j] = -1
            else:
                matrix[i][j] = 0
            idx += 1

    result = [0] * n
    possible_values = [[] for _ in range(n)]

    # 🔽 미리 가능한 값 줄이기
    for i in range(n):
        if matrix[i][i] == 0:
            possible_values[i] = [0]
        elif matrix[i][i] == 1:
            possible_values[i] = list(range(1, 11))
        else:
            possible_values[i] = list(range(-10, 0))

    prefix_sum = [0] * (n + 1)  # 누적합 배열

    def is_valid(pos):
        # 🔍 pos번째까지 확인된 누적합을 이용해 구간합 검사
        for i in range(pos + 1):
            total = prefix_sum[pos + 1] - prefix_sum[i]
            if total > 0 and matrix[i][pos] != 1:
                return False
            if total < 0 and matrix[i][pos] != -1:
                return False
            if total == 0 and matrix[i][pos] != 0:
                return False
        return True

    def backtrack(pos):
        if pos == n:
            print(*result)
            sys.exit()
        for val in possible_values[pos]:
            result[pos] = val
            prefix_sum[pos + 1] = prefix_sum[pos] + val
            if is_valid(pos):
                backtrack(pos + 1)

    backtrack(0)

solution()
