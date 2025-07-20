import sys

# 전역 스코프에 주요 변수와 함수를 배치하여 성능 향상
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]  # 1x1 ~ 5x5 색종이의 남은 개수
min_count = float('inf')

def can_attach(x, y, size):
    """(x, y)를 좌상단 꼭짓점으로 하여 size 크기의 색종이를 붙일 수 있는지 확인"""
    # 범위 검사
    if x + size > 10 or y + size > 10:
        return False
    # 덮을 영역에 0이 포함되어 있는지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] == 0:
                return False
    return True

def attach(x, y, size, state):
    """색종이를 붙이거나(0으로 덮기) 떼는(1로 복구) 함수"""
    for i in range(x, x + size):
        for j in range(y, y + size):
            paper[i][j] = state

def backtracking(x, y, count):
    """
    (x, y)부터 시작하여 다음에 덮어야 할 '1'을 찾아 탐색하는 함수
    """
    global min_count

    # 가지치기: 현재 사용한 종이 수가 이미 찾은 최솟값보다 크면 중단
    if count >= min_count:
        return

    # --- 핵심 최적화: 다음에 덮어야 할 1을 찾아 점프 ---
    # y부터 탐색 시작하여 x행의 끝까지
    for j in range(y, 10):
        if paper[x][j] == 1:
            nx, ny = x, j
            break
    else: # x행에서 1을 못 찾았다면 다음 행부터 탐색
        for i in range(x + 1, 10):
            for j in range(10):
                if paper[i][j] == 1:
                    nx, ny = i, j
                    break
            else: # 현재 행에서도 1을 못 찾았으면 다음 행으로
                continue
            break # 바깥쪽 for문도 탈출
        else: # 모든 칸을 다 확인했는데 1이 없다면 (모두 덮음)
            min_count = min(min_count, count)
            return
    # ---------------------------------------------------

    # 찾은 '1'의 위치(nx, ny)에 가장 큰 색종이부터 붙여본다
    for size in range(5, 0, -1):
        if papers[size] > 0 and can_attach(nx, ny, size):
            attach(nx, ny, size, 0) # 색종이 붙이기 (1 -> 0)
            papers[size] -= 1
            
            # 다음 '1'을 찾아 재귀 호출
            backtracking(nx, ny, count + 1)
            
            # 상태 복구 (백트래킹)
            papers[size] += 1
            attach(nx, ny, size, 1) # 붙였던 색종이 떼기 (0 -> 1)


# (0, 0)에서 탐색 시작
backtracking(0, 0, 0)

# 결과 출력
print(min_count if min_count != float('inf') else -1)