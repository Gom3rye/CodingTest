import sys
from collections import defaultdict
input = sys.stdin.readline
def solution():
    t = int(input()) # <=100
    for _ in range(t):
        n = int(input()) # #의상 0<= <=30
        if n == 0:
            print(0)
            continue
        clothes = defaultdict(int)
        # 여기서 중요한 건 종류! 이름이 아니라
        for _ in range(n):
            _, kind = input().split()
            clothes[kind] += 1

        # 종류마다 이 옷을 고를 건지 안 고를건지 선택하는 모든 경우의 수 - 아무것도 안 고른 경우(1)
        answer = 1
        for cnt in clothes.values():
            answer *= (cnt+1)
        print(answer-1)
solution()