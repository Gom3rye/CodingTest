import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input()) # #gear <=1000
    # rotate 함수 쓰기 위해 deque로 선언!
    gears = [deque(map(int, input().strip())) for _ in range(n)]
    def rotation(id, dir):
        # 0번 기어-> 2번, k-1번 기어->6번/ 그 사이 기어들은 2,6번 모두 확인해야 함
        need_to_rotate = [0]*n # 회전 방향 기록하기
        need_to_rotate[id] = dir
    
        # id기준으로 왼쪽 확인
        target = id
        left = id-1
        left_dir = dir # 새 변수로 원본 데이터 변하지 않도록
        while left >= 0:
            # 같은 극이면 빠져나오기
            if gears[target][6] == gears[left][2]:
                break
            need_to_rotate[left] = -left_dir
            left_dir = -left_dir # 1-> -1, -1-> 1
            target = left
            left -= 1 # 더 왼쪽으로

        # id기준으로 오른족 확인
        target = id
        right = id+1
        right_dir = dir
        while right < n:
            if gears[target][2] == gears[right][6]:
                break
            need_to_rotate[right] = -right_dir
            right_dir = -right_dir
            target = right
            right += 1 # 더 오른쪽으로

        # 한 꺼번에 모든 톱니바퀴가 회전해야 한다.
        for i in range(n):
            dir = need_to_rotate[i]
            if dir != 0:
                gears[i].rotate(dir)
    
    k = int(input()) # #회전 <=1000
    for _ in range(k):
        id, dir = map(int, input().split()) # 1:cw, -1:ccw
        rotation(id-1, dir) # id: 0based index
    print(sum(gears[i][0] for i in range(n)))
solution()