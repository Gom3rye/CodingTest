import sys
from math import log2
input = sys.stdin.readline
def solution():
    n, d, k, c = map(int, input().split()) # #접시 <=30000, 초밥종류 <=3000, 윈도우 <=3000, 쿠폰번호
    # 최대 초밥 가짓수
    sushis = [int(input()) for _ in range(n)]
    # 슬라이딩 윈도우 초기 구성
    count = [0]*(d+1) # count[sushi]: 윈도우에 있는 sushi의 개수
    count[c] += 1 # 공짜 스시 저장
    kind = 1
    for i in range(k):
        if count[sushis[i]] == 0:
            kind += 1
        count[sushis[i]] += 1

    # 윈도우 한칸씩 돌려가면 계산
    max_kind = kind
    for i in range(n-1):
        remove = sushis[i]
        count[remove] -= 1
        if count[remove] == 0:
            kind -= 1
        add = sushis[(i+k)%n]
        if count[add] == 0:
            kind += 1
        count[add] += 1
        # kind 갱신
        max_kind = max(max_kind, kind)
        if max_kind == k+1:
            break
    print(max_kind)
solution()