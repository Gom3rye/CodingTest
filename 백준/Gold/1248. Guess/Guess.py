import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    sign = input().strip()
    matrix = [[None]*n for _ in range(n)]
    # matrix 초기화 (계산의 편의를 위해 +는 1로, -는 -1로, 0은 0으로 초기화)
    idx = 0
    for i in range(n):
        for j in range(i, n):
            if sign[idx] == '+':
                matrix[i][j] = 1
            elif sign[idx] == '-':
                matrix[i][j] = -1
            else:
                matrix[i][j] = 0
            idx += 1
    
    result = [0]*n # 정답 수열을 미리 0으로 초기화 해놓자.
    def is_valid(idx):
        total = 0
        # 모든 검사를 다 한 후 틀린 게 없어야지만 참이니 False 조건을 먼저 가지치기해야 한다.
        for i in range(idx, n):
            total += result[i]
            if total > 0 and matrix[idx][i] != 1:
                return False
            elif total < 0 and matrix[idx][i] != -1:
                return False
            elif total == 0 and matrix[idx][i] != 0:
                return False
            
        return True

    def backtracking(idx):
        if idx < 0:
            print(*result)
            sys.exit()

        for i in range(-10, 11):
            result[idx] = i
            # 누적합으로 타당성을 검증해서 맞는 것만 다음 백트레킹 진행
            if is_valid(idx):
                backtracking(idx-1)

    backtracking(n-1)
solution()