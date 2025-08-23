import sys
from collections import deque

def solution():
    # 1. 톱니바퀴 상태 입력 (deque 리스트로 저장)
    gears = [deque(map(int, sys.stdin.readline().strip())) for _ in range(4)]
    K = int(sys.stdin.readline())

    # 2. K번의 회전 명령 처리
    for _ in range(K):
        gear_idx, direction = map(int, sys.stdin.readline().split())
        gear_idx -= 1  # 0-indexed로 변환

        # 3-a. 어떤 톱니가 회전할지 미리 결정
        rotations = [0] * 4
        rotations[gear_idx] = direction

        # 3-c. 오른쪽으로 연쇄 반응 확인
        for i in range(gear_idx, 3):
            # 현재 톱니(i)의 오른쪽(2)과 다음 톱니(i+1)의 왼쪽(6) 극이 다르면
            if gears[i][2] != gears[i+1][6]:
                # 다음 톱니는 반대 방향으로 회전
                rotations[i+1] = -rotations[i]
            else:
                # 극이 같으면 연쇄 반응 중단
                break
        
        # 3-d. 왼쪽으로 연쇄 반응 확인
        for i in range(gear_idx, 0, -1):
            # 현재 톱니(i)의 왼쪽(6)과 이전 톱니(i-1)의 오른쪽(2) 극이 다르면
            if gears[i][6] != gears[i-1][2]:
                # 이전 톱니는 반대 방향으로 회전
                rotations[i-1] = -rotations[i]
            else:
                # 극이 같으면 연쇄 반응 중단
                break

        # 3-e. 결정된 회전을 한 번에 적용
        for i in range(4):
            if rotations[i] != 0:
                gears[i].rotate(rotations[i])

    # 4. 최종 점수 계산
    score = 0
    for i in range(4):
        # 12시 방향(인덱스 0)이 S극(1)이면 점수 추가
        if gears[i][0] == 1:
            score += 2**i
    
    print(score)

solution()