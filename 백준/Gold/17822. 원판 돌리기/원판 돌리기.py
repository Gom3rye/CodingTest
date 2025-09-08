from collections import deque
import sys

def solution():
    # 입력 받기
    N, M, T = map(int, sys.stdin.readline().split())
    disks = [deque(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    # T번의 회전 명령 실행
    for _ in range(T):
        x, d, k = map(int, sys.stdin.readline().split())
        
        # 1. 원판 회전
        for i in range(N):
            # 원판 번호는 i+1
            if (i + 1) % x == 0:
                if d == 0:  # 시계 방향
                    disks[i].rotate(k)
                else:  # 반시계 방향
                    disks[i].rotate(-k)

        # 2. 인접하면서 같은 수 찾기
        # 삭제할 좌표를 저장할 집합
        to_delete = set()
        
        # 2-1. 같은 원판 내에서 인접한 수 찾기
        for i in range(N):
            for j in range(M):
                if disks[i][j] != 0 and disks[i][j] == disks[i][(j + 1) % M]:
                    to_delete.add((i, j))
                    to_delete.add((i, (j + 1) % M))

        # 2-2. 다른 원판과 인접한 수 찾기
        for j in range(M):
            for i in range(N - 1):
                if disks[i][j] != 0 and disks[i][j] == disks[i+1][j]:
                    to_delete.add((i, j))
                    to_delete.add((i + 1, j))

        # 3. 삭제 또는 평균 조정
        if to_delete:
            # 3-1. 삭제할 수가 있는 경우
            for r, c in to_delete:
                disks[r][c] = 0
        else:
            # 3-2. 삭제할 수가 없는 경우
            total_sum = 0
            count = 0
            for i in range(N):
                for j in range(M):
                    if disks[i][j] != 0:
                        total_sum += disks[i][j]
                        count += 1
            
            # 원판에 남은 수가 있을 때만 평균 조정
            if count > 0:
                avg = total_sum / count
                for i in range(N):
                    for j in range(M):
                        if disks[i][j] != 0:
                            if disks[i][j] > avg:
                                disks[i][j] -= 1
                            elif disks[i][j] < avg:
                                disks[i][j] += 1

    # 4. 최종 합계 계산
    final_sum = 0
    for i in range(N):
        final_sum += sum(disks[i])
        
    print(final_sum)

solution()