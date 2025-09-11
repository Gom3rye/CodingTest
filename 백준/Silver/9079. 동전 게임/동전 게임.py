import sys
from collections import deque

# 하나의 테스트 케이스를 푸는 함수
def solve():
    # 1. 초기 상태 입력 및 변환
    initial_grid = [sys.stdin.readline().split() for _ in range(3)]
    # set에 넣기 위해 불변 자료형인 tuple로 변환
    initial_state = tuple(map(tuple, initial_grid))
    
    # 목표 상태 정의
    all_H = tuple(tuple('H' for _ in range(3)) for _ in range(3))
    all_T = tuple(tuple('T' for _ in range(3)) for _ in range(3))

    # 2. BFS 준비
    q = deque([(initial_state, 0)]) # (상태, 연산 횟수)
    visited = {initial_state}

    # 3. BFS 실행
    while q:
        current_state, count = q.popleft()

        # 목표 상태 도달 시 종료
        if current_state == all_H or current_state == all_T:
            print(count)
            return

        # 8가지 연산을 적용하여 다음 상태 생성
        # 0~2: 행 뒤집기, 3~5: 열 뒤집기, 6: 주 대각선, 7: 부 대각선
        for i in range(8):
            # 다음 상태를 만들기 위해 임시로 list로 변환
            grid = [list(row) for row in current_state]

            if i < 3: # 행 뒤집기
                for j in range(3):
                    grid[i][j] = 'H' if grid[i][j] == 'T' else 'T'
            elif i < 6: # 열 뒤집기
                col = i - 3
                for j in range(3):
                    grid[j][col] = 'H' if grid[j][col] == 'T' else 'T'
            elif i == 6: # 주 대각선 뒤집기
                for j in range(3):
                    grid[j][j] = 'H' if grid[j][j] == 'T' else 'T'
            else: # 부 대각선 뒤집기
                for j in range(3):
                    grid[j][2-j] = 'H' if grid[j][2-j] == 'T' else 'T'
            
            # 다시 tuple로 변환하여 다음 상태 생성
            next_state = tuple(map(tuple, grid))
            
            # 아직 방문하지 않은 상태라면 큐에 추가
            if next_state not in visited:
                visited.add(next_state)
                q.append((next_state, count + 1))

    # 큐가 비었는데 목표에 도달 못했다면 불가능
    print(-1)


# 메인 로직: 테스트 케이스 수만큼 solve 함수 호출
T = int(sys.stdin.readline())
for _ in range(T):
    solve()