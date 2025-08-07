import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    chocolates = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                chocolates.append((i, j))
    result = []
    for x, y in chocolates: # 떼어낼 초콜릿 정하기
        # 검사할 초콜릿 빠른 검색을 위해 set으로 생성
        choco = set(chocolates)
        choco.remove((x,y))
        
        # 조건1. 한 덩어리인지 탐색
        start = next(iter(choco))
        q = deque([start])
        visited = {start} # visited=set(start) 하면 set은 iterable을 만들어서 안됨
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            cx, cy = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+cx, dy+cy
                if (nx, ny) not in visited and (nx, ny) in choco:
                    visited.add((nx, ny))
                    q.append((nx, ny))

        if len(choco) != len(visited):
            continue # 한 덩어리가 아니라는 소리니까

        # 조건2: 트리 구조인지 탐색
        v = len(choco)
        e = 0
        for cx, cy in choco:
            # 중복 탐색을 방지하기 위해 오른쪽, 아래쪽만 탐색
            if (cx+1, cy) in choco:
                e += 1
            if (cx, cy+1) in choco:
                e += 1
        if v-e==1:
            result.append((x+1, y+1))
    
    print(len(result))
    for x, y in result:
        print(x, y)
solution()