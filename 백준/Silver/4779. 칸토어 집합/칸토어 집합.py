import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    def cantoring(n):
        if n == 0:
            return '-'
        prev_length = 3**(n-1)
        # n-1단계의 결과를 재귀로 가져옴
        prev_result = cantoring(n-1)
        # 가운데 공백 생성
        middle_space = ' '*prev_length
        # n-1 결과 + 공백 + n-1 결과
        return prev_result+middle_space+prev_result
        
    try:
        while True:
            n = int(input())
            answer = cantoring(n)
            print(answer)
    except:
        return           
solution()