import sys
input = sys.stdin.readline

def solution():
    N, M, L, K = map(int, input().split())
    stars = [tuple(map(int, input().split())) for _ in range(K)]

    max_hit = 0

    # 트램펄린의 왼쪽 아래 좌표를 별 좌표 기준으로만 잡는다
    for x, _ in stars:
        for _, y in stars:
            cnt = 0
            for sx, sy in stars:
                if x <= sx <= x + L and y <= sy <= y + L:
                    cnt += 1
            max_hit = max(max_hit, cnt)

    print(K - max_hit)

solution()
