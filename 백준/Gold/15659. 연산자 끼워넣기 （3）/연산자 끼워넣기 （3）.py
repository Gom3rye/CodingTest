import sys
from itertools import permutations

# 입력 받기
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
op_counts = list(map(int, sys.stdin.readline().split())) # +, -, *, / 의 개수

# 연산자 리스트 만들기
operators = []
op_map = {0: '+', 1: '-', 2: '*', 3: '/'}
for i in range(4):
    operators.extend([op_map[i]] * op_counts[i])

# 초기 최댓값과 최솟값 설정
max_result = -1_000_000_001 # -10억보다 1 작은 값
min_result = 1_000_000_001  # 10억보다 1 큰 값

# N-1개의 연산자로 만들 수 있는 모든 순열을 구하고, set으로 중복 제거
unique_op_perms = set(permutations(operators, N - 1))

# 각각의 연산자 순열 조합에 대해 결과 계산
for op_perm in unique_op_perms:
    # 식 만들기 (예: "1+2*3-4")
    expression = str(numbers[0])
    for i in range(N - 1):
        expression += op_perm[i] + str(numbers[i+1])
    
    # 문제의 나눗셈은 정수 나눗셈이므로 '/'를 '//'로 변경
    expression = expression.replace('/', '//')
    
    # eval 함수로 연산자 우선순위를 고려하여 식 계산
    current_result = eval(expression)
    
    # 최댓값과 최솟값 갱신
    max_result = max(max_result, current_result)
    min_result = min(min_result, current_result)

# 결과 출력
print(max_result)
print(min_result)