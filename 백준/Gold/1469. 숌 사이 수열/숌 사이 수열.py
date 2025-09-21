import sys

def solve(idx):
    # [성공 조건] 모든 칸을 다 채웠다면 성공
    if idx == 2 * N:
        print(*result)
        sys.exit(0) # 답을 찾았으므로 프로그램 즉시 종료

    # 현재 칸이 이미 채워져 있다면 다음 칸으로 이동
    if result[idx] != -1:
        solve(idx + 1)
        return

    # [탐색] 정렬된 X의 원소들(작은 숫자)부터 시도
    for num in X:
        # [가지치기 1] 이미 사용한 숫자인가?
        if used[num]:
            continue
        
        # 두 번째 숫자를 놓을 위치
        pair_idx = idx + num + 1
        
        # [가지치기 2] 두 번째 숫자를 놓을 위치가 유효한가?
        if pair_idx >= 2 * N or result[pair_idx] != -1:
            continue
            
        # [선택] 숫자 쌍을 배치
        result[idx] = num
        result[pair_idx] = num
        used[num] = True
        
        # [다음 단계] 재귀 호출
        solve(idx + 1)
        
        # [백트래킹] 선택을 취소하고 원상 복구
        result[idx] = -1
        result[pair_idx] = -1
        used[num] = False

# --- 메인 로직 ---
N = int(sys.stdin.readline())
# ★ 사전 순 출력을 위해 반드시 정렬!
X = sorted(list(map(int, sys.stdin.readline().split())))

result = [-1] * (2 * N)
used = [False] * 17 # X의 원소는 최대 16

# 0번 인덱스부터 탐색 시작
solve(0)

# 여기까지 코드가 도달했다면 답을 찾지 못한 것이므로 -1 출력
print(-1)