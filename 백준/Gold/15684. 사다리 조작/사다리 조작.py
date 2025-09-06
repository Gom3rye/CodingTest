import sys

def solution():
    input = sys.stdin.readline
    N, M, H = map(int, input().split())
    
    # ladder[h][n] -> n번 세로선과 n+1번 세로선을 h번 위치에서 연결
    ladder = [[False] * (N + 1) for _ in range(H + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        ladder[a][b] = True

    def check():
        """모든 i번 세로선이 i번으로 도착하는지 확인"""
        for start_col in range(1, N + 1):
            current_col = start_col
            for row in range(1, H + 1):
                if ladder[row][current_col]:  # 오른쪽으로 이동
                    current_col += 1
                elif ladder[row][current_col - 1]:  # 왼쪽으로 이동
                    current_col -= 1
            if current_col != start_col:
                return False
        return True

    def dfs(start_idx, count, target_cnt):
        """
        target_cnt 개의 사다리를 놓는 모든 조합을 탐색
        start_idx: 조합을 만들 때 중복을 피하기 위한 시작 위치
        """
        nonlocal answer
        
        # 목표 개수만큼 사다리를 다 놓았다면
        if count == target_cnt:
            if check():
                answer = target_cnt # 성공했다면 answer 갱신
            return

        # (r, c)에 사다리를 놓는 것을 시도
        # start_idx를 이용해 이전에 탐색한 위치는 다시 보지 않음
        for i in range(start_idx, H + 1):
            for j in range(1, N):
                # 연속된 가로선은 놓을 수 없음
                if ladder[i][j] or ladder[i][j - 1] or ladder[i][j + 1]:
                    continue
                
                ladder[i][j] = True
                dfs(i, count + 1, target_cnt)
                ladder[i][j] = False

                # ★★★ 중요 ★★★
                # 정답을 찾았다면 더 이상 탐색할 필요가 없으므로 즉시 종료
                if answer != -1:
                    return

    answer = -1
    # 0개부터 3개까지 차례대로 시도
    for i in range(4):
        dfs(1, 0, i)
        if answer != -1:
            break
            
    print(answer)

solution()