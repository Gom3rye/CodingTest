import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    # 입력이 '123'처럼 공백 없이 들어오므로, 각 문자를 숫자로 변환
    board = [list(map(int, list(input().strip()))) for _ in range(N)]

    # 1. 2차원 누적 합 테이블 생성
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            prefix_sum[r][c] = board[r-1][c-1] + prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1]

    # O(1) 시간에 특정 사각형의 합을 구하는 함수
    def get_sum(r1, c1, r2, c2):
        return prefix_sum[r2+1][c2+1] - prefix_sum[r1][c2+1] - prefix_sum[r2+1][c1] + prefix_sum[r1][c1]

    max_product = 0

    # 2. 모든 6가지 분할 패턴에 대해 완전 탐색
    
    # 패턴 1: 세로로만 3등분 (세로줄 2개로 자름)
    for c1 in range(M - 2):
        for c2 in range(c1 + 1, M - 1):
            s1 = get_sum(0, 0, N - 1, c1)
            s2 = get_sum(0, c1 + 1, N - 1, c2)
            s3 = get_sum(0, c2 + 1, N - 1, M - 1)
            max_product = max(max_product, s1 * s2 * s3)

    # 패턴 2: 가로로만 3등분 (가로줄 2개로 자름)
    for r1 in range(N - 2):
        for r2 in range(r1 + 1, N - 1):
            s1 = get_sum(0, 0, r1, M - 1)
            s2 = get_sum(r1 + 1, 0, r2, M - 1)
            s3 = get_sum(r2 + 1, 0, N - 1, M - 1)
            max_product = max(max_product, s1 * s2 * s3)

    # 패턴 3: 세로로 한번 자른 뒤, 왼쪽을 가로로 자름 (ㅏ 모양)
    for c in range(M - 1):
        for r in range(N - 1):
            s1 = get_sum(0, 0, r, c)
            s2 = get_sum(r + 1, 0, N - 1, c)
            s3 = get_sum(0, c + 1, N - 1, M - 1)
            max_product = max(max_product, s1 * s2 * s3)

    # 패턴 4: 세로로 한번 자른 뒤, 오른쪽을 가로로 자름 (ㅓ 모양)
    for c in range(M - 1):
        for r in range(N - 1):
            s1 = get_sum(0, 0, N - 1, c)
            s2 = get_sum(0, c + 1, r, M - 1)
            s3 = get_sum(r + 1, c + 1, N - 1, M - 1)
            max_product = max(max_product, s1 * s2 * s3)

    # 패턴 5: 가로로 한번 자른 뒤, 위쪽을 세로로 자름 (ㅗ 모양)
    for r in range(N - 1):
        for c in range(M - 1):
            s1 = get_sum(0, 0, r, c)
            s2 = get_sum(0, c + 1, r, M - 1)
            s3 = get_sum(r + 1, 0, N - 1, M - 1)
            max_product = max(max_product, s1 * s2 * s3)
            
    # 패턴 6: 가로로 한번 자른 뒤, 아래쪽을 세로로 자름 (ㅜ 모양)
    for r in range(N - 1):
        for c in range(M - 1):
            s1 = get_sum(0, 0, r, M - 1)
            s2 = get_sum(r + 1, 0, N - 1, c)
            s3 = get_sum(r + 1, c + 1, N - 1, M - 1)
            max_product = max(max_product, s1 * s2 * s3)

    print(max_product)
    
solution()