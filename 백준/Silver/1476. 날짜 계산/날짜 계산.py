import sys
input = sys.stdin.readline
def solution():
    E, S, M = map(int, input().split()) # 지구, 태양, 달
    # 각각의 주기가 다르기 때문에 모두 딱 나눠떨어지는 때가 언제인지 구하기
    now = 1 # 현재는 1년
    while True:
        if (now-E)%15 == (now-S)%28 == (now-M)%19 == 0: # 모두 나뉘어 떨어질 때
            print(now)
            break
        now += 1
solution()