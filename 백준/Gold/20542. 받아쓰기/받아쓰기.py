import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    seungyeon = input().strip()
    answer = input().strip()
    # i는 i,j,l과 매칭/ v는 w와 매칭
    # 편집 거리 알고리즘: dp[i][j] = sy[0~i-1] → ans[0~j-1]로 바꾸는 최소 수정 횟수
    # dp[i-1][j-1], dp[i-1][j], dp[i][j-1] 세 값만 참조하므로 이전 행(prev)과 현재 행(curr) 두 줄만 있으면 충분
    prev = list(range(m+1)) # 이전 행 dp[i-1][*]
    curr = [0]*(m+1) # 현재 행 dp[i][*]
    def correct(sy, ans):
        if sy == ans:
            return True
        elif sy == 'i' and ans in "jl":
            return True
        elif sy == 'v' and ans == 'w':
            return True
        else:
            return False
    
    for i in range(1, n+1):
        curr[0] = i # dp[i][0]: ans가 빈 문자열일 때 (삭제 i번)
        for j in range(1, m+1):
            if correct(seungyeon[i-1], answer[j-1]):
                curr[j] = prev[j-1] # 같으면 추가 연산 없음
            else:
                curr[j] = min(
                    prev[j], # 삭제
                    curr[j-1], # 추가
                    prev[j-1] # 변환
                )+1
        curr, prev = prev, curr # swap
    print(prev[-1])
solution()