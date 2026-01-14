import sys
input = sys.stdin.readline
def solution():
    k = int(input()) # 먹어야 하는 초콜릿 수 <=1,000,000
    # 구매해야 하는 가장 작은 초콜릿의 크기와 최소 몇 번 쪼개야 하는지
    # 그리디: 항상 큰 조각부터 필요하면 먹고 필요 없으면 쪼갠다.
    # 쪼갠 횟수를 최소화하기 위해 k크기만큼을 확보했으면 그만 쪼개기
    chocolate = 1
    # 구매할 초콜릿 크기 구하기
    while chocolate < k:
        chocolate *= 2
    # 딱 k라면 쪼갤 필요 없음
    if chocolate == k:
        print(chocolate, 0)
        return
    # 쪼개기 시뮬레이션
    size = chocolate
    cnt = 0
    remain = k # 현재 조각
    while remain > 0:
        size //= 2 # 큰 덩이부터
        cnt += 1
        if remain >= size:
            remain -= size

    print(chocolate, cnt)
solution()