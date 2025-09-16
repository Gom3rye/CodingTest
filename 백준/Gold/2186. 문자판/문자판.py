import sys

def solution():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    board = [input().strip() for _ in range(N)]
    word = input().strip()
    
    word_len = len(word)
    
    # dp[r][c]: 현재 처리 중인 글자를 (r,c)에서 완성하는 경로의 수
    # 첫 글자로 DP 테이블 초기화
    dp = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if board[r][c] == word[0]:
                dp[r][c] = 1

    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 단어의 두 번째 글자부터 마지막 글자까지 순회하며 dp 테이블을 갱신
    for i in range(1, word_len):
        # 현재 글자에 대한 경로 수를 계산할 새 dp 테이블
        new_dp = [[0] * M for _ in range(N)]
        
        # 이전 글자(i-1)의 dp 테이블을 순회
        for r in range(N):
            for c in range(M):
                # 이전 단계에서 해당 위치로 올 수 있는 경로가 없었다면 건너뛰기
                if dp[r][c] == 0:
                    continue
                
                # (r,c)에서 K칸까지 이동 가능한 모든 곳을 탐색
                for j in range(4): # 4방향
                    for k in range(1, K + 1): # 1~K칸 거리
                        nr, nc = r + dx[j] * k, c + dy[j] * k
                        
                        if 0 <= nr < N and 0 <= nc < M:
                            # 현재 우리가 찾아야 할 글자(word[i])와 일치하면
                            if board[nr][nc] == word[i]:
                                # (r,c)에서 출발하는 경로의 수(dp[r][c])만큼
                                # (nr,nc)에 도달하는 경로의 수가 늘어남
                                new_dp[nr][nc] += dp[r][c]
        
        # 다음 글자 계산을 위해 dp 테이블을 새 것으로 교체
        dp = new_dp
        
    # 마지막으로 계산된 dp 테이블의 모든 값을 합산
    print(sum(map(sum, dp)))

solution()