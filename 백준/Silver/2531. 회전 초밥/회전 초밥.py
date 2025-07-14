import sys
input = sys.stdin.readline
def solution():
    n, d, k, c = map(int, input().split()) # 접시 수, 초밥 수, 연속해서 먹는 접시 수, 쿠폰 번호
    sushi = [int(input()) for _ in range(n)]
    # 종류별 개수 저장
    count = [0]*(d+1)
    kind = 0
    # 초기 윈도우 구성
    for i in range(k):
        if count[sushi[i]] == 0:
            kind += 1
        count[sushi[i]] += 1
    # max_kind 초기화
    max_kind = kind + (1 if count[c] == 0 else 0)

    # 슬라이딩 윈도우
    for start in range(1, n):
        # 왼쪽 초밥 제거
        left = sushi[start-1]
        count[left] -= 1
        if count[left] == 0:
            kind -= 1
        # 오른쪽 초밥 추가
        right = sushi[(start+k-1)%n] # mod로 회전 처리
        if count[right] == 0:
            kind += 1
        count[right] += 1

        # 쿠폰 초밥 확인
        now = kind + (1 if count[c] == 0 else 0)
        max_kind = max(max_kind, now)
    print(max_kind)
solution()