import sys
input = sys.stdin.readline

def solution():
    R, C, M = map(int, input().split())
    board = [[None] * C for _ in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r - 1][c - 1] = [s, d, z]

    # 방향 정보 (0-indexed로 다루기 편하게 변경)
    # 0:상, 1:하, 2:우, 3:좌
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 입력 d(1~4)를 dx,dy 인덱스(0~3)로 변환하는 맵
    d_map = {1: 0, 2: 1, 3: 2, 4: 3}
    
    # 방향 전환을 위한 맵 (상↔하, 우↔좌)
    d_rev = [1, 0, 3, 2]

    score = 0

    for fisher_col in range(C):
        # 1. 낚시
        for i in range(R):
            if board[i][fisher_col]:
                score += board[i][fisher_col][2]
                board[i][fisher_col] = None
                break
        
        # 2. 상어 이동
        new_board = [[None] * C for _ in range(R)]
        for r_idx in range(R):
            for c_idx in range(C):
                if board[r_idx][c_idx]:
                    s, d_orig, z = board[r_idx][c_idx]
                    d = d_map[d_orig] # 방향을 0~3 인덱스로 변환
                    nr, nc = r_idx, c_idx

                    if d < 2: # 상하 이동
                        cycle = (R - 1) * 2
                        if cycle > 0:
                            s %= cycle
                        
                        # O(1) 계산
                        # 1. 이동 거리를 더함
                        final_pos = nr + s * dx[d]
                        # 2. divmod로 몫과 나머지 계산
                        quotient, remainder = divmod(final_pos, R - 1)
                        # 3. 몫에 따라 최종 위치와 방향 결정
                        if quotient % 2 == 0:
                            nr = remainder
                        else:
                            nr = (R - 1) - remainder
                            d = d_rev[d]

                    else: # 좌우 이동
                        cycle = (C - 1) * 2
                        if cycle > 0:
                            s %= cycle
                        
                        final_pos = nc + s * dy[d]
                        quotient, remainder = divmod(final_pos, C - 1)
                        if quotient % 2 == 0:
                            nc = remainder
                        else:
                            nc = (C - 1) - remainder
                            d = d_rev[d]
                    
                    # 3. 포식 처리
                    if new_board[nr][nc]:
                        if z > new_board[nr][nc][2]:
                            # 방향은 1~4로 다시 변환해서 저장
                            new_board[nr][nc] = [s, list(d_map.keys())[list(d_map.values()).index(d)], z]
                    else:
                        new_board[nr][nc] = [s, list(d_map.keys())[list(d_map.values()).index(d)], z]
        
        board = new_board
        
    print(score)

solution()