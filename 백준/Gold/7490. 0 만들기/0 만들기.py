import sys
input = sys.stdin.readline
# Space < + < - 순으로 아스키코드
# print(ord(' ')) # 32
# print(ord("+")) # 43
# print(ord("-")) # 45
def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        num = list(map(str, range(1, n+1))) # 빈칸 연산 쉽게 하기 위해서 문자열로 생성
        def backtracking(expression, idx):
            if idx > n:
                tmp = expression.replace(' ', '')
                if eval(tmp) == 0:
                    print(expression)
                return
            # 빈칸인 경우
            backtracking(expression+' '+str(idx), idx+1)
            # +인 경우
            backtracking(expression+'+'+str(idx), idx+1)
            # -인 경우
            backtracking(expression+'-'+str(idx), idx+1)
        backtracking('1', 2) # 표현식은 1부터 시작하고 다음 숫자는 2부터 시작
        print() # 한 줄 띄워 구분한다.

solution()