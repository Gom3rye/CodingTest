import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sy = input()
answer = input()
matrix = [[0] * (n+1) for _ in range(m+1)]
for i in range(m+1):
    matrix[i][0] = i
for j in range(n+1):
    matrix[0][j] = j
 
for i in range(1, m+1):
    for j in range(1, n+1):
        if answer[i-1] == sy[j-1]:
            matrix[i][j] = matrix[i-1][j-1]
        elif sy[j-1] == 'i' and (answer[i-1] == 'j' or answer[i-1] == 'l'):   # 휘갈겨 쓴 i
            matrix[i][j] = matrix[i-1][j-1]
        elif sy[j-1] == 'v' and (answer[i-1] == 'w'):   # 휘갈겨 쓴 v
            matrix[i][j] = matrix[i-1][j-1]
        else:
            matrix[i][j] = min(matrix[i-1][j], matrix[i]
                               [j-1], matrix[i-1][j-1]) + 1
print(matrix[m][n])