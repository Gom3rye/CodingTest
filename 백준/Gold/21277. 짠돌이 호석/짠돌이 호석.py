import sys
input = sys.stdin.readline
INF = float('inf')

# 1. 퍼즐을 시계방향 90도 회전하는 함수
def rotate(puzzle):
    N = len(puzzle)
    M = len(puzzle[0])
    new_puzzle = [['0'] * N for _ in range(M)]
    for r in range(N):
        for c in range(M):
            new_puzzle[c][N - 1 - r] = puzzle[r][c]
    return new_puzzle

# 2. 두 퍼즐이 (dr, dc) 오프셋으로 겹치는지 확인하는 함수
def check_overlap(p1, p2, dr, dc):
    N1, M1 = len(p1), len(p1[0])
    N2, M2 = len(p2), len(p2[0])
    
    for r2 in range(N2):
        for c2 in range(M2):
            # P2가 '1'인 칸에 대해서만 검사
            if p2[r2][c2] == '1':
                # P1에 대응되는 좌표
                r1, c1 = r2 + dr, c2 + dc
                
                # P1 범위 안이고, P1도 '1'이면 겹침
                if (0 <= r1 < N1 and 0 <= c1 < M1 and p1[r1][c1] == '1'):
                    return True
    return False # 겹치지 않음

# 3. 퍼즐 읽는 함수
def read_puzzle():
    N, M = map(int, input().split())
    puzzle = [list(input().strip()) for _ in range(N)]
    return puzzle

# --- 메인 로직 ---

p1 = read_puzzle()
p2 = read_puzzle()

# 4. 각 퍼즐의 4가지 회전 버전을 미리 생성
p1_rotations = []
current_p1 = p1
for _ in range(4):
    p1_rotations.append(current_p1)
    current_p1 = rotate(current_p1)

p2_rotations = []
current_p2 = p2
for _ in range(4):
    p2_rotations.append(current_p2)
    current_p2 = rotate(current_p2)

min_area = INF

# 5. 4(P1) * 4(P2) = 16가지 회전 조합 순회
for p1_rot in p1_rotations:
    for p2_rot in p2_rotations:
        
        N1, M1 = len(p1_rot), len(p1_rot[0])
        N2, M2 = len(p2_rot), len(p2_rot[0])

        # 6. 모든 상대 위치 (dr, dc) 시도
        # (범위를 여유롭게 -N2 ~ N1, -M2 ~ M1)
        for dr in range(-N2, N1 + 1):
            for dc in range(-M2, M1 + 1):
                
                # 7. 겹치지 않는다면 넓이 계산
                if not check_overlap(p1_rot, p2_rot, dr, dc):
                    
                    # 8. 바운딩 박스(Bounding Box) 계산
                    min_r = min(0, dr)
                    max_r = max(N1 - 1, dr + N2 - 1)
                    min_c = min(0, dc)
                    max_c = max(M1 - 1, dc + M2 - 1)
                    
                    H = max_r - min_r + 1
                    W = max_c - min_c + 1
                    
                    min_area = min(min_area, H * W)

print(min_area)