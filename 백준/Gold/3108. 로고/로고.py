import sys
from itertools import combinations
input = sys.stdin.readline
def solution():
    # 직사각형 n개를 그리는데 필요한 pu명령(펜을 떼는 것)의 최솟값 구하기
    n = int(input()) # 직사각형의 개수 <=1000
    # 0,0에서 펜을 내린 채 출발하는 거니까 0,0(점)인 rect도 넣어주기
    rectangles = [[0,0,0,0]]+[list(map(int, input().split())) for _ in range(n)]
    parents = list(range(n+1))
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parents[b] = a
    # 좌표가 겹치면 pu명령 추가 없이 직사각형을 그릴 수 있으므로 겹치는지 여부 조사
    def meet(recta, rectb):
        ax1, ay1, ax2, ay2 = recta
        bx1, by1, bx2, by2 = rectb
        
        # 두 직사각형이 서로 떨어져 있는 경우
        if ax2 < bx1 or ay2 < by1 or bx2 < ax1 or by2 < ay1:
            return False
        # 한 직사각형이 다른 직사각형을 포함하고 있는 경우
        # a가 바깥 - b가 안
        if ax1 < bx1 and ay1 < by1 and bx2 < ax2 and by2 < ay2:
            return False
        # b가 바깥 - a가 안
        if bx1 < ax1 and by1 < ay1 and ax2 < bx2 and ay2 < by2:
            return False
        
        return True

    for comb in combinations(range(n+1), 2):
        a, b = comb
        # 두 사각형이 겹치면 union
        if meet(rectangles[a], rectangles[b]):
            union(a, b)

    # 모든 부모 루트로 압축
    for i in range(n+1):
        parents[i] = find(i)
    root_set = set(parents)
    print(len(root_set)-1) # 0그룹 하나 제거
solution()