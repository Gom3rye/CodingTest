import sys
input = sys.stdin.readline

# 메모이제이션용 3차원 배열 생성 (0~20 까지만 사용)
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = (
            w(a-1, b, c)
            + w(a-1, b-1, c)
            + w(a-1, b, c-1)
            - w(a-1, b-1, c-1)
        )
    return dp[a][b][c]

def solution():
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        result = w(a, b, c)
        print(f"w({a}, {b}, {c}) = {result}")

solution()
