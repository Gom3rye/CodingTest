import sys
input = sys.stdin.readline
def solution():
    # 최대한 많은 별똥별을 튕겨내도록 배치했을 때 지구에 떨어지는 별똥별 수
    m, n, l, k = map(int, input().split()) # col, row <=500,000, 트램펄린 길이 <=100,000, #별똥별 <=100
    # 별똥별의 개수가 최대 100으로 충분히 작으므로 완탐!
    stars = [list(map(int, input().split())) for _ in range(k)]
    max_cnt = 0
    for sx, _ in stars:
        for _, sy in stars:
            cnt = 0
            for x, y in stars:
                if sx<=x<=sx+l and sy<=y<=sy+l:
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
    print(k-max_cnt)
solution()