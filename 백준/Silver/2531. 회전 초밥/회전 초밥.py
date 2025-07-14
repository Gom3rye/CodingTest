import sys
input = sys.stdin.readline

def solution():
    n, d, k, c = map(int, input().split())  # 접시 수, 초밥 종류 수, 연속해서 먹는 수, 쿠폰 초밥 번호
    sushi = [int(input()) for _ in range(n)]

    # 초밥 종류별 개수 저장 (1~d번까지 초밥 종류)
    count = [0] * (d + 1)
    unique = 0  # 현재 윈도우 내의 고유 초밥 수

    # 초기 윈도우 구성
    for i in range(k):
        if count[sushi[i]] == 0:
            unique += 1
        count[sushi[i]] += 1

    # 쿠폰 고려
    max_kind = unique + (1 if count[c] == 0 else 0)

    # 슬라이딩 윈도우
    for i in range(1, n):
        # 제거되는 초밥
        remove = sushi[(i - 1) % n]
        count[remove] -= 1
        if count[remove] == 0:
            unique -= 1

        # 추가되는 초밥
        add = sushi[(i + k - 1) % n]
        if count[add] == 0:
            unique += 1
        count[add] += 1

        # 쿠폰 초밥이 포함 안되었으면 +1
        current_kind = unique + (1 if count[c] == 0 else 0)
        max_kind = max(max_kind, current_kind)

    print(max_kind)

solution()
