import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    # 사이클을 가능하게 하는 지점을 떼어내야 조건을 만족할 수 있다.

    # 1. 초콜릿들 위치 저장
    chocolates = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                chocolates.append((i, j))
    
    choco = len(chocolates)
    answers = []
    # 2. 각 초콜릿을 한 번씩 떼어보는 시뮬레이션
    for i in range(choco):
        removed = chocolates[i]

        # 떼어낸 후 남은 초콜릿들의 집합 (빠른 조회를 위해 set사용)
        remaining = set(chocolates)
        remaining.remove(removed)

        # 조건1. 연결성 확인 (bfs)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        # remaining이 set이라 순서가 없으니 맨 앞 하나 꺼내려면 이렇게 해야 한다.
        start = next(iter(remaining))
        q = deque([start])
        visited = {start}
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if (nx, ny) in remaining and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))

        # bfs 후 방문한 개수가 남은 초콜릿 수와 다르면 조각이 나뉜 것
        if len(visited) != len(remaining):
            continue

        # 조건2. 사이클 확인 (v-e=1)
        v = len(remaining)
        e = 0
        # 간선 개수 세기 (중복 방지를 위해 오른쪽, 아래쪽만 확인)
        for x, y in remaining:
            if (x, y+1) in remaining: # 오른쪽 확인
                e += 1
            if (x+1, y) in remaining: # 아래쪽 확인
                e += 1
        
        # 연결 그래프가 트리이려면 v-e=1 이어야 한다.
        if v-e == 1:
            # 두 조건 모두 만족시 정답에 추가 (좌표는 1based index)
            answers.append((removed[0]+1, removed[1]+1))
    
    # 최종 출력
    print(len(answers))
    for x, y in answers:
        print(x, y)

solution()