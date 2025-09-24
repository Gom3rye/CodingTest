import sys
from itertools import combinations
input = sys.stdin.readline
def backtracking(idx, game, team_result):
    if idx == 15: # 모든 경기를 탐색했으면
        return True
    
    i, j = game[idx]
    wi, ti, li = team_result[i]
    wj, tj, lj = team_result[j]
    # i팀이 이겼을 경우
    if wi > 0 and lj > 0:
        team_result[i][0] -= 1
        team_result[j][2] -= 1
        if backtracking(idx+1, game, team_result):
            return True
        team_result[i][0] += 1
        team_result[j][2] += 1
    # i팀과 j팀이 비겼을 경우
    if ti > 0 and tj > 0:
        team_result[i][1] -= 1
        team_result[j][1] -= 1
        if backtracking(idx+1, game, team_result):
            return True
        team_result[i][1] += 1
        team_result[j][1] += 1
    # i팀이 졌을 경우
    if li > 0 and wj > 0:
        team_result[i][2] -= 1
        team_result[j][0] -= 1
        if backtracking(idx+1, game, team_result):
            return True
        team_result[i][2] += 1
        team_result[j][0] += 1
    return False
def solution():
    # 가능한 결과가 되려면 승과 패의 합이 같아야 하고 무승부의 총합이 짝수여야 한다.
    for _ in range(4):
        result = list(map(int, input().split()))
        # 나라별로
        team_result = [result[3*i:3*i+3] for i in range(6)]

        # '각 나라의 승+무+패 != 5' or '모든 나라의 총 승 != 총 패 or 무승부의 개수가 홀수'면 불가능
        total_win, total_tie, total_lose = 0, 0, 0
        for i in range(6):
            if sum(team_result[i]) != 5:
                print(0, end=' ')
                break
            total_win += team_result[i][0]
            total_tie += team_result[i][1]
            total_lose += team_result[i][2]

        else:
            if (total_win != total_lose) or (total_tie%2 != 0):
                print(0, end=' ')
                continue

            # 백트레킹으로 15개의 모든 경기 탐색
            game = list(combinations(range(6), 2))
            if backtracking(0, game, team_result):
                print(1, end=' ')
            else:
                print(0, end=' ')

solution()