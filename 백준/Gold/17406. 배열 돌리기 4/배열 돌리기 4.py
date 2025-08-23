import sys
from itertools import permutations
from copy import deepcopy

input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())
    # 원본 배열 저장
    original_board = [list(map(int, input().split())) for _ in range(N)]
    # K개의 회전 연산 정보 저장
    rotations = [list(map(int, input().split())) for _ in range(K)]

    min_value = float('inf')

    # 1. itertools.permutations를 이용해 모든 회전 순서를 생성
    for p in permutations(rotations, K):
        # 2. 각 순서를 시도할 때마다 원본 배열의 복사본으로 시작
        board = deepcopy(original_board)
        
        # 현재 순서(p)에 따라 회전 연산을 차례로 수행
        for r, c, s in p:
            r, c = r - 1, c - 1 # 0-based index로 변환
            
            # (r,c,s)에 해당하는 정사각형들을 회전
            for i in range(1, s + 1):
                # 각 정사각형의 가장 왼쪽 위 좌표
                top, left = r - i, c - i
                bottom, right = r + i, c + i
                
                # 시작점 값 임시 저장
                temp = board[top][left]

                # 왼쪽 변 -> 위쪽 변 (아래에서 위로)
                for row in range(top, bottom):
                    board[row][left] = board[row + 1][left]
                
                # 아래쪽 변 -> 왼쪽 변 (오른쪽에서 왼쪽으로)
                for col in range(left, right):
                    board[bottom][col] = board[bottom][col + 1]
                
                # 오른쪽 변 -> 아래쪽 변 (위에서 아래로)
                for row in range(bottom, top, -1):
                    board[row][right] = board[row - 1][right]

                # 위쪽 변 -> 오른쪽 변 (왼쪽에서 오른쪽으로)
                for col in range(right, left, -1):
                    board[top][col] = board[top][col - 1]
                
                board[top][left + 1] = temp

        # 3. 현재 순서의 모든 회전이 끝난 후 배열의 '값' 계산
        for row in board:
            min_value = min(min_value, sum(row))

    print(min_value)

solution()