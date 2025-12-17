import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #지점 <=50,000
    # 원형의 공간에서 두 탑을 세우고 이 거리가 최대가 되도록
    dist = list(int(input()) for _ in range(n))
    # max(min(d, total-d)) => 최대가 되려면 최대한 d가 total/2에 가까운 연속 구간을 찾아야 한다.
    total = sum(dist)
    mid = total/2
    d, end, answer = 0, 0, 0
    for start in range(n):
        while d < mid:
            d += dist[end]
            end = (end+1)%n
        answer = max(answer, min(total-d, d))
        d -= dist[start]
    print(answer)
solution()