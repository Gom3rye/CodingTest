import sys
input = sys.stdin.readline
def solution():
    answer = list(map(int, input().split()))
    # dp 상태 정의 잘하기 dp[idx][prev1][prev2][score]: 이 상태를 가지고 있는 경우의 수
    dp = [[[[-1]*11 for _ in range(6)] for _ in range(6)] for _ in range(10)]
    def dfs(idx, prev1, prev2, score):
        if idx == 10:
            if score >= 5:
                return 1
            return 0
        
        # memoization
        if dp[idx][prev1][prev2][score] != -1: # 초기 상황이 아니라면
            return dp[idx][prev1][prev2][score]
        
        total = 0
        for choices in range(1, 6):
            if prev1 == prev2 == choices:
                continue
            if answer[idx] == choices:
                total += dfs(idx+1, choices, prev1, score+1)
            else:
                total += dfs(idx+1, choices, prev1, score)

        dp[idx][prev1][prev2][score] = total
        return total

    print(dfs(0, 0, 0, 0)) # idx, prev1, prev2, score
    
solution()