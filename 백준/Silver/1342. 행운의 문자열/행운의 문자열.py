import sys
from collections import Counter

input = sys.stdin.readline

def solution():
    s = input().strip()
    n = len(s)
    
    # 문자의 종류와 개수를 세어 관리
    counts = Counter(s)
    
    # DP 테이블(메모) 역할을 할 딕셔너리
    dp = {}

    # char_map: 문자에 인덱스를 부여하여 튜플 상태를 일관되게 관리
    # 예: {'a': 0, 'b': 1}
    char_map = {char: i for i, char in enumerate(counts.keys())}
    
    # 초기 남은 문자 개수를 튜플로 생성
    initial_counts_tuple = tuple(counts[char] for char in char_map)

    def solve(prev_char_idx, remaining_counts):
        # 성공 조건: 모든 문자를 다 사용했다면 1가지 방법을 찾은 것
        if sum(remaining_counts) == 0:
            return 1

        # 현재 상태를 튜플로 정의 (DP 테이블의 key로 사용)
        state = (prev_char_idx, remaining_counts)
        
        # 메모이제이션: 이미 계산된 상태라면 저장된 값 반환
        if state in dp:
            return dp[state]

        total = 0
        # 사용할 수 있는 문자 종류를 순회
        for char, char_idx in char_map.items():
            # 이전 문자와 현재 문자가 다르고, 사용할 문자가 남아있다면
            if char_idx != prev_char_idx and remaining_counts[char_idx] > 0:
                
                # 다음 상태의 remaining_counts를 튜플로 생성
                # (튜플은 불변이므로 리스트로 변환 후 수정하고 다시 튜플로 만듦)
                next_counts_list = list(remaining_counts)
                next_counts_list[char_idx] -= 1
                next_counts_tuple = tuple(next_counts_list)
                
                total += solve(char_idx, next_counts_tuple)

        # DP 테이블에 현재 상태의 결과 저장
        dp[state] = total
        return total

    # 초기 호출: 이전 문자는 없는 상태(-1), 초기 문자 개수 튜플로 시작
    # (문자열 길이가 아닌 남은 문자 개수로 종료를 판별하므로 idx는 필요 없음)
    result = solve(-1, initial_counts_tuple)
    print(result)

solution()