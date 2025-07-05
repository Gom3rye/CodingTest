import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    s = list(input().split())
    min_result = ''
    max_result = ''
    visited = [False]*10 # 0~9 숫자 방문 체크
    def valid(a,b,op):
        if op == '<':
            return a<b
        else:
            return a>b
        
    def backtracking(depth, path):
        nonlocal max_result, min_result
        if depth == n+1:
            num = ''.join(map(str, path))
            if not min_result:
                min_result = num
            max_result = num
            return
        for i in range(10):
            if not visited[i]:
                if depth == 0 or valid(path[-1], i, s[depth-1]):
                    visited[i] = True
                    backtracking(depth+1, path+[i])
                    visited[i] = False
    backtracking(0, [])
    print(max_result)
    print(min_result)
solution()