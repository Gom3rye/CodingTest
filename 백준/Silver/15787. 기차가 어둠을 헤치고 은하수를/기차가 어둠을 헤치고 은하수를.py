import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    # N개의 기차 상태를 0으로 초기화 (20비트 정수)
    trains = [0] * N

    for _ in range(M):
        command = list(map(int, input().split()))
        cmd_type = command[0]
        
        if cmd_type == 1:
            i, x = command[1] - 1, command[2] - 1
            # x번째 비트를 1로 설정 (OR)
            trains[i] |= (1 << x)
        
        elif cmd_type == 2:
            i, x = command[1] - 1, command[2] - 1
            # x번째 비트를 0으로 설정 (AND NOT)
            trains[i] &= ~(1 << x)

        elif cmd_type == 3:
            i = command[1] - 1
            # 모든 비트를 왼쪽으로 1칸씩 이동
            trains[i] <<= 1
            # 20번째 비트를 넘어가는 값(21번째 승객)은 0으로 처리 (하차)
            trains[i] &= (1 << 20) - 1

        else: # cmd_type == 4
            i = command[1] - 1
            # 모든 비트를 오른쪽으로 1칸씩 이동 (1번째 승객은 자동 하차)
            trains[i] >>= 1

    # 최종적으로 기록된 기차 상태들 중에서 중복을 제거
    passed_trains = set()
    for train_state in trains:
        passed_trains.add(train_state)
        
    print(len(passed_trains))

solution()