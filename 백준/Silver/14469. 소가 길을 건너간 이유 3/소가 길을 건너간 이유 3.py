import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    cows = []
    for _ in range(n):
        arrival, questioning = map(int, input().split())
        cows.append((arrival, questioning))
    cows.sort(key=lambda x: x[0])
    now = 0
    for arrival, questioning in cows:
        if now < arrival:
            now = arrival # 소가 도착했을 때까지 기다림
        now += questioning # 검문 시간 추가
    print(now)
solution()