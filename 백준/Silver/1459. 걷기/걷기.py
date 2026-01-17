import sys
input = sys.stdin.readline
def solution():
    x, y, w, s = map(int, input().split()) # 집위치 <=1,000,000,000, 직진시간, 대각선시간 <=10000
    # x,y가 너무 크니까 bfs불가 -> 그리디로
    # x가 큰 쪽, y가 작은 쪽으로 고정
    if x < y:
        x, y = y, x
    # 대각선으로만 가는 경우
    # 1. x-y가 홀수인 경우-> 남은 1번은 직선으로
    if (x-y)%2 == 1:
        diag = (x-1)*s+w
    # 2. x-y가 짝수인 경우-> 모두 대각 가능
    else:
        diag = x*s
    # 대각선+직선으로 가는 경우
    both = y*s+(x-y)*w
    # 직선으로만 가는 경우
    straight = (x+y)*w
    print(min(diag, both, straight))
solution()