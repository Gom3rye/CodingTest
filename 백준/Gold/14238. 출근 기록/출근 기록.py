import sys
input = sys.stdin.readline
def solution():
    s = input().strip()
    n = len(s)
    # n>=50으로 크기 때문에 메모이제이션도 써야 한다. 이때 순열로 하면(순서0) 메모이제이션 못 쓰니까 a,b,c를 쓴 개수를 기록하며 개수 기반 상태를 만들자.
    dp = {} # dp[status] = T/F
    acnt, bcnt, ccnt = s.count('A'), s.count('B'), s.count('C')
    result = []
    # backtracking + dp = if backtracking(): 구조로 짜야됨
    def backtracking(a, b, c, prev, pprev):
        if a+b+c == n:
            return True
        
        # memoization 사용
        if (a, b, c, prev, pprev) in dp: # (현재 상태)
            return dp[(a, b, c, prev, pprev)]

        if a < acnt:
            result.append('A')
            if backtracking(a+1, b, c, 'A', prev): # prev가 지금 넣은 'A'가 되고 pprev이 prev로 (다음 상태)
                # memoization 기록
                dp[(a, b, c, prev, pprev)] = True # (현쟂 상태 기록)
                return True
            result.pop()

        if b < bcnt and prev != 'B':
            result.append('B')
            if backtracking(a, b+1, c, 'B', prev):
                dp[(a, b, c, prev, pprev)] = True
                return True
            result.pop()
        
        if c < ccnt and prev != 'C' and pprev != 'C':
            result.append('C')
            if backtracking(a, b, c+1, 'C', prev):
                dp[(a, b, c, prev, pprev)] = True
                return True
            result.pop()
        
        # 메모이제이션 기록은 상태 복구의 일환이 아니라 모든 분기 처리 후 어떤 것도 성공하지 못했을때 기록해야 한다.
        dp[(a, b, c, prev, pprev)] = False
        return False
        
    if backtracking(0,0,0,-1,-1): # 그전, 그전전은 -1로 표시
        print("".join(result))
    else:
        print(-1)
solution()