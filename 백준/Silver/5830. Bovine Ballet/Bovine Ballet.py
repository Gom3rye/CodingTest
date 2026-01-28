import sys
def solution():
    n = int(sys.stdin.readline())
    # 발 순서: FL, FR, RL, RR
    feet = {'FL': [0, 1], 'FR': [1, 1], 'RL': [0, 0], 'RR': [1, 0]}
    order = ['FL', 'FR', 'RL', 'RR']
    facing = 0  # 0:N, 1:E, 2:S, 3:W
    
    # 방향에 따른 전진(F) 벡터
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 전체 영역 기록용
    min_x = max_x = 0
    min_y = max_y = 1 # 초기 위치 포함
    # 초기 위치들을 미리 반영
    for f in order:
        min_x = min(min_x, feet[f][0])
        max_x = max(max_x, feet[f][0])
        min_y = min(min_y, feet[f][1])
        max_y = max(max_y, feet[f][1])

    for _ in range(n):
        inst = sys.stdin.readline().strip()
        f_id = inst[:2]
        action = inst[2]
        
        if action == 'P':
            # 피벗 수행
            px, py = feet[f_id]
            for fid in order:
                if fid == f_id: continue
                ox, oy = feet[fid]
                # 시계방향 90도 회전 공식
                feet[fid] = [px + (oy - py), py - (ox - px)]
            facing = (facing + 1) % 4
        else:
            # 이동 방향 결정
            move_dir = facing
            if action == 'B': move_dir = (facing + 2) % 4
            elif action == 'R': move_dir = (facing + 1) % 4
            elif action == 'L': move_dir = (facing + 3) % 4
            
            feet[f_id][0] += dx[move_dir]
            feet[f_id][1] += dy[move_dir]
            
        # 겹침 체크
        current_pos = [tuple(feet[f]) for f in order]
        if len(set(current_pos)) < 4:
            print("-1")
            return
            
        # 영역 확장
        for f in order:
            min_x = min(min_x, feet[f][0])
            max_x = max(max_x, feet[f][0])
            min_y = min(min_y, feet[f][1])
            max_y = max(max_y, feet[f][1])
            
    print((max_x - min_x + 1) * (max_y - min_y + 1))

solution()