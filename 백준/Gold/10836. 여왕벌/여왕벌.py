import sys
input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())

    # 경계 길이: 왼쪽 열(M) + 위쪽 행(M-1)
    size = 2 * M - 1
    border = [0] * size

    # N일 동안 경계 성장 누적
    for _ in range(N):
        zero, one, two = map(int, input().split())
        idx = zero
        for _ in range(one):
            border[idx] += 1
            idx += 1
        for _ in range(two):
            border[idx] += 2
            idx += 1

    # 결과 격자 출력
    # (i, j)의 값 = 1 + max(왼쪽 경계, 위쪽 경계)
    for i in range(M):
        row = []
        for j in range(M):
            if j == 0:
                grow = border[M - 1 - i]   # 왼쪽 열 (아래 → 위)
            else:
                grow = border[M - 1 + j]     # 위쪽 행
            row.append(str(1 + grow))
        print(" ".join(row))

solution()