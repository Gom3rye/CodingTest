import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solution():
    n = int(input()) 
    marbles = dict()
    for i in range(n):
        marbles[i] = int(input())

    # 1. dp를 set이 아닌 dict로 변경
    #    (state: result)를 저장해야 함
    dp = {} 
    
    def dfs(m, prev, pprev):
        if sum(m.values()) == 0:
            return 1
        
        # 2. state를 'tuple'로 만들어 hashable하게 변경
        #    dict.items()의 순서를 보장하기 위해 sorted() 사용
        state = (tuple(sorted(m.items())), prev, pprev)
        
        # 3. memoization 확인: dp에 state가 있으면, 
        #    저장된 '값(dp[state])'을 반환
        if state in dp:
            return dp[state]
        
        cnt = 0
        for i in range(n):
            if m[i] > 0 and i != prev and i != pprev:
                m[i] -= 1
                cnt += dfs(m, i, prev)
                m[i] += 1 # 백트래킹 (원상 복구)
        
        # 4. memoization 저장: state의 '결과(cnt)'를 저장
        dp[state] = cnt
        return cnt
        
    print(dfs(marbles, -1, -2))

solution()