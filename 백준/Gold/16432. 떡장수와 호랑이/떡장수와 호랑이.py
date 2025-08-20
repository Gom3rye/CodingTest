import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solution():
    n = int(input())
    # info[i]: i번째 날에 동희가 가진 떡의 목록 (0based index)
    info = [list(map(int, input().split()))[1:] for _ in range(n)]
    # dp[idx][prev_tt]: idx-1일에 prev_tt떡을 줬을 때 idx일부터 끝까지 생존 가능한지 여부. (미확인: -1, 가능: 1, 불가능: 0)
    dp = [[-1]*10 for _ in range(n)]
    # 최종 경로를 저장할 리스트
    tteoks = [0]*n
    def backtracking(idx, prev_tt):
        # 종료 조건: 모든 날짜를 통과했으면 생존 성공
        if idx == n:
            return True
        
        # memoization
        if dp[idx][prev_tt] != -1:
            return dp[idx][prev_tt] == 1 # 가능(1)이면 True로, 불가능(0)이면 False로 반환

        # 백트레킹
        for tt in info[idx]:
            if tt != prev_tt:
                if backtracking(idx+1, tt):
                    tteoks[idx] = tt # 현재 선택을 경로에 기록
                    dp[idx][prev_tt] = 1 # 현재 상태 생존 가능(1)로 기록
                    return True # 성공 신호를 위로 전달
        
        # for문 다 돌았는데 성공 경로 찾지 못한 경우
        dp[idx][prev_tt] = 0 # 생존 불가능으로 기록
        return False # 실패 신호를 위로 전달

    if backtracking(0, -1): # 아직 줄 떡 못 정했으니까 -1로
        for tt in tteoks:
            print(tt)
    else:
        print(-1)

solution()