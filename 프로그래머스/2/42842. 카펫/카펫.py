import sys
from math import sqrt
input = sys.stdin.readline
def solution(brown, yellow):
    answer = []
    total = brown+yellow
    # 약수 구할 때 sqrt까지만 돌려보면 된다.
    # 항상 세로가 가로보다 더 짧거나 같아야 하므로 세로를 작은 수부터 탐색
    for bx in range(3, int(sqrt(total))+1): # 안에 yellow가 들어가야 하므로 bx는 최소 3부터 시작
        by = total // bx
        if (bx-2)*(by-2) == yellow:
            answer = [by, bx]
            break
    return answer