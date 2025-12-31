import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #전구, 스위치 <=100,000
    current = list(map(int, input().strip()))
    final = list(map(int, input().strip()))
    INF = float('inf')
    answer = INF # 최소 횟수 구하는 거니까
    def toggle(bulb, i):
        for th in (i-1, i, i+1):
            if 0<=th<n:
                bulb[th] ^= 1 # toggle
        return bulb
    # 전구 i-1을 바꿀 수 있는 마지막 스위치가 i번 -> i-1번째가 다르면 i번째 스위치를 무조건 눌러야 함
    # 첫번째 전구를 누를지 말지 결정하는 것부터 시작
    for first in (False, True): # 안 누르기, 누르기
        bulbs = current[:]
        cnt = 0
        if first:
            toggle(bulbs, 0)
            cnt += 1
        # 1번째부터 누를지 안 누를지 검색
        for i in range(1, n):
            if bulbs[i-1] != final[i-1]:
                toggle(bulbs, i)
                cnt += 1

        if bulbs == final:
            answer = min(answer, cnt)

    print(answer if answer != INF else -1)
solution()