import sys
N = int(sys.stdin.readline())
cal = list(sys.stdin.readline().strip())
result = -1*2**31 # 최솟값

def calculate(a, op, b):
    if op=='+':
        num = a + b
    elif op=='*':
        num = a * b
    elif op == '-':
        num = a - b
    return num   

def dfs(index, value):
    global result

    if index == N - 1:
        result = max(result, value)
        return

    if index + 2 < N:
        # 다음번에 나오는 수와 계산하는데, 다음번에 나오는 수가 괄호가 쳐져있지 않을 때
        next_value = calculate(value, cal[index + 1], int(cal[index + 2])) 
        dfs(index + 2, next_value) # 다음번에 나오는 수와 계산했기 때문에 index+2, 다음번에 나오는 수까지 계산한 결과를 파라미터로 넣어줌

    if index + 4 < N:
        # 다음번에 나오는 수와 계산하는데, 다음번에 나오는 수가 다다음번에 나오는 수와 괄호가 쳐져있을 때
        next_next_value = calculate(int(cal[index+2]), cal[index+3], int(cal[index+4])) # 괄호 처리(다음번 수 (+, *, -) 다다음번 수)
        next_value = calculate(value, cal[index + 1], next_next_value) # 다음번에 나오는 수
        dfs(index + 4, next_value) # index + 4까지 계산 끝났기 때문에 index + 4, 현재까지의 결과를 파라미터로 넣어줌

dfs(0, int(cal[0]))
print(result)