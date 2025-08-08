import sys
input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())
    laptop = [[0] * M for _ in range(N)]

    for _ in range(K):
        R, C = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(R)]

        # 4번 회전 시도
        for _ in range(4):
            is_attached = False
            sticker_r, sticker_c = len(sticker), len(sticker[0])
            
            # 노트북의 모든 위치를 시도
            for r in range(N - sticker_r + 1):
                for c in range(M - sticker_c + 1):
                    # 1. 스티커를 붙일 수 있는지 (겹치는지) 확인
                    if all(laptop[r + i][c + j] == 0 for i in range(sticker_r) for j in range(sticker_c) if sticker[i][j] == 1):
                        
                        # 2. 붙일 수 있다면, 스티커 부착
                        for i in range(sticker_r):
                            for j in range(sticker_c):
                                if sticker[i][j] == 1:
                                    laptop[r + i][c + j] = 1
                        is_attached = True
                        break
                if is_attached:
                    break
            
            # 3. 스티커를 붙였다면 다음 스티커로
            if is_attached:
                break
            
            # 4. 못 붙였다면 시계방향 90도 회전
            sticker = [list(row) for row in zip(*sticker[::-1])]

    # 5. 최종적으로 붙은 스티커 칸의 개수 계산
    print(sum(map(sum, laptop)))

solution()