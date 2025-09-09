import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m, t = map(int, input().split()) # 반지름, 원판에 적인 수의 개수, 회전 횟수
    circles = [0]+[deque(map(int, input().split())) for _ in range(n)] # 1based index
    for _ in range(t):
        x, d, k = map(int, input().split()) # 번호가 x의 배수인 원판을 d방향(0:시계, 1:반시계)으로 k칸 회전
        if d == 1:
            k = -k
        for i in range(x, n+1, x): # x의 배수만
            circles[i].rotate(k)
        # 인접하면서 수가 같은 것 모두 찾기 (set에 넣어놔서 한 번에 0처리, 개별적으로 해주면 코드 길어짐)
        tobedeleted = set()
        # 같은 원판 내에서 인접
        for i in range(1, n+1):
            for j in range(m):
                target = circles[i][j]
                if target == 0:
                    continue
                if target == circles[i][(j+1)%m]:
                    tobedeleted.add((i, j))
                    tobedeleted.add((i, (j+1)%m))
        # 다른 원판끼리 인접
        for j in range(m):
            for i in range(1, n):
                target = circles[i][j]
                if target == 0:
                    continue
                if target == circles[i+1][j]:
                    tobedeleted.add((i, j))
                    tobedeleted.add((i+1, j))
        # 지울 것이 있다면
        if tobedeleted:
            for x, y in tobedeleted:
                circles[x][y] = 0
        else:
            # 원판에 적힌 수의 평균을 구하고 평균보다 큰 수에서 -1, 작은 수에는 +1
            avg, cnt = 0, 0
            for i in range(1, n+1):
                for j in range(m):
                    if circles[i][j] != 0:
                        cnt += 1
                        avg += circles[i][j]
            # 원판에 남은 수가 있을 때만 평균 조정
            if cnt > 0: # 이 코드 없으면 ZeroDivisionError 난다.
                avg /= cnt
                for i in range(1, n+1):
                    for j in range(m):
                        if circles[i][j] == 0:
                            continue
                        if circles[i][j] < avg:
                            circles[i][j] += 1
                        elif circles[i][j] > avg:
                            circles[i][j] -= 1
    # 총합 구하기        
    score = 0
    for i in range(1, n+1):
        score += sum(circles[i])
    print(score)      
solution()