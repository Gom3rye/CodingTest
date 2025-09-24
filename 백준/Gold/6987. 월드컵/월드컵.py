import sys
from itertools import combinations

def solve(game_idx):
    # [성공 조건] 15경기를 모두 성공적으로 배정했다면 가능한 경우
    if game_idx == 15:
        return True

    team1, team2 = games[game_idx]

    # 선택 1: team1 승, team2 패
    if records[team1][0] > 0 and records[team2][2] > 0:
        records[team1][0] -= 1
        records[team2][2] -= 1
        if solve(game_idx + 1):
            return True
        # 백트래킹 (원상 복구)
        records[team1][0] += 1
        records[team2][2] += 1

    # 선택 2: team1 무, team2 무
    if records[team1][1] > 0 and records[team2][1] > 0:
        records[team1][1] -= 1
        records[team2][1] -= 1
        if solve(game_idx + 1):
            return True
        # 백트래킹 (원상 복구)
        records[team1][1] += 1
        records[team2][1] += 1

    # 선택 3: team1 패, team2 승
    if records[team1][2] > 0 and records[team2][0] > 0:
        records[team1][2] -= 1
        records[team2][0] += 1
        if solve(game_idx + 1):
            return True
        # 백트래킹 (원상 복구)
        records[team1][2] += 1
        records[team2][0] -= 1
    
    # 세 가지 선택 모두 실패했다면 불가능
    return False

# 15개의 모든 경기 조합을 미리 생성
games = list(combinations(range(6), 2))
answers = []

# 4개의 테스트 케이스에 대해 반복
for _ in range(4):
    input_data = list(map(int, sys.stdin.readline().split()))
    
    # 입력을 [승, 무, 패] 6팀의 2차원 리스트로 변환
    records = [input_data[i*3 : i*3+3] for i in range(6)]
    
    # 1. 간단한 조건으로 미리 확인
    is_valid = True
    total_wins = sum(r[0] for r in records)
    total_draws = sum(r[1] for r in records)
    total_losses = sum(r[2] for r in records)

    # 총 승수 != 총 패수 이거나, 총 무승부가 홀수이면 불가능
    if total_wins != total_losses or total_draws % 2 != 0:
        is_valid = False

    # 각 팀의 (승+무+패)가 5가 아니면 불가능
    if is_valid:
        for r in records:
            if sum(r) != 5:
                is_valid = False
                break
    
    # 2. 간단한 조건을 통과했다면 백트래킹으로 최종 확인
    if is_valid and solve(0):
        answers.append("1")
    else:
        answers.append("0")

print(" ".join(answers))