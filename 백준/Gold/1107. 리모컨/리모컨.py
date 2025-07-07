import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 이동하려는 채널
    m = int(input()) # 고장난 버튼의 개수
    if m != 0:
        b = set(map(str, input().split())) # 고장난 버튼들을 담는 리스트
    else:
        b = set()
    # +,-만 사용하는 경우
    min_clicks = abs(n-100) # 현재 위치가 100이니까

    # 모든 가능한 채널 탐색 (n의 최대가 50만이니까 백만까지)
    for c in range(1000000):
        channel = str(c)
        can_press = True
        for digit in channel:
            if digit in b:
                can_press = False
                break
        if can_press:
            # (숫자 버튼 누르는 횟수) + (+,- 누르는 횟수)
            clicks = len(channel)+abs(n-c)
            if clicks < min_clicks:
                min_clicks = clicks
    print(min_clicks)

solution()