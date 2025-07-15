import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    signs = input().strip()

    sign_matrix = [[0]*n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(i, n):
            if signs[idx] == '+':
                sign_matrix[i][j] = 1
            elif signs[idx] == '-':
                sign_matrix[i][j] = -1
            else:
                sign_matrix[i][j] = 0
            idx += 1

    result = [0] * n

    def is_valid(pos):
        total = 0
        for i in range(pos, -1, -1):
            total += result[i]
            if total > 0 and sign_matrix[i][pos] != 1:
                return False
            elif total < 0 and sign_matrix[i][pos] != -1:
                return False
            elif total == 0 and sign_matrix[i][pos] != 0:
                return False
        return True

    def backtrack(pos):
        if pos == n:
            print(' '.join(map(str, result)))
            sys.exit()  # 첫 해답만 출력하고 종료
        for num in range(-10, 11):
            result[pos] = num
            if is_valid(pos):
                backtrack(pos + 1)

    backtrack(0)
solution()