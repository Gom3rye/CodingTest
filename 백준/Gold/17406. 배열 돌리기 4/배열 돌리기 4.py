import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    rotations = [list(map(int, input().split())) for _ in range(k)]
    min_result = float('inf')
    def count(grid):
        return min(map(sum, grid))
    # 회전하는 함수
    def rotate(x, y, s, temp):
        x -=1
        y -=1 # 0based index로 만들기
        for size in range(1, s+1):
            # 꼭짓점 정보를 위한 상하좌우
            left, right, top, bottom = y-size, y+size, x-size, x+size

            # 시작값 저장
            tmp = temp[top][left]

            # 왼쪽 변 -> 위쪽 변 (아래에서 위로)
            for row in range(top, bottom):
                temp[row][left] = temp[row+1][left]
            
            # 아래쪽 변 -> 왼쪽 변 (오른쪽에서 왼쪽으로)
            for col in range(left, right):
                temp[bottom][col] = temp[bottom][col+1]
            
            # 오른쪽 변 -> 아래쪽 변 (위에서 아래로)
            for row in range(bottom, top, -1):
                temp[row][right] = temp[row-1][right]

            # 위쪽 변 -> 오른쪽 변 (왼쪽에서 오른쪽으로)
            for col in range(right, left, -1):
                temp[top][col] = temp[top][col-1]
            
            temp[top][left+1] = tmp
            

    for perm in permutations(rotations, k):
        temp = [row[:] for row in board]
        for x, y, s in perm:
            rotate(x, y, s, temp)
        min_result = min(min_result, count(temp))
    print(min_result)    

solution()
