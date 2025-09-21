import sys

# 입력 받기
S = sys.stdin.readline().strip()
L = len(S)

# 상태 변수 초기화
result = [] # 복원된 순열을 저장할 리스트
# 사용한 숫자를 체크 (순열은 1부터 시작, 최대 50)
used = [False] * 51 

def solve(idx):
    # [성공 조건] 문자열 끝까지 모두 사용했다면
    if idx == L:
        # 완성된 순열이 1부터 N까지 모두 포함하는지 최종 확인
        N = len(result)
        is_permutation = True
        for i in range(1, N + 1):
            if not used[i]: # 만약 1~N 사이의 숫자가 사용되지 않았다면
                is_permutation = False
                break
        
        if is_permutation:
            print(*result)
            sys.exit(0) # 답을 하나 찾으면 프로그램 즉시 종료
        return

    # --- [재귀 탐색] ---
    
    # 선택 1: 한 글자 자르기
    num1 = int(S[idx])
    # [가지치기] 사용한 적 없는 숫자라면
    if not used[num1]:
        # 선택
        result.append(num1)
        used[num1] = True
        # 다음 단계로 진행
        solve(idx + 1)
        # 백트래킹 (원상 복구)
        used[num1] = False
        result.pop()

    # 선택 2: 두 글자 자르기 (문자열 범위를 벗어나지 않는 경우)
    if idx + 1 < L:
        num2 = int(S[idx:idx+2])
        # [가지치기] 50 이하이고, 사용한 적 없는 숫자라면
        if num2 <= 50 and not used[num2]:
            # 선택
            result.append(num2)
            used[num2] = True
            # 다음 단계로 진행 (두 글자를 사용했으므로 idx+2)
            solve(idx + 2)
            # 백트래킹 (원상 복구)
            used[num2] = False
            result.pop()

# 0번 인덱스부터 탐색 시작
solve(0)