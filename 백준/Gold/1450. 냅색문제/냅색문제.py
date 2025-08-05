import sys
input = sys.stdin.readline
from itertools import combinations
from bisect import bisect_right
def solution():
    n, c = map(int, input().split()) # n개의 물건, 가방에 최대 c만큼의 무게를 넣을 수 있다.
    weights = list(map(int, input().split()))
    # 2**30 -> 약 10**9(10억)로 시간초가 나기 때문에 반으로 나누기
    a = weights[:n//2]
    b = weights[n//2:] # n이 홀수라면 len(a) < len(b)
    # a, b그룹의 부분집합의 합을 모두 구하기
    suma = []
    sumb = []
    # i개수만큼 골라서 부분집합 만들기
    for i in range(len(a)+1): # 0개(공집합) ~ len(a)개(전체) 고를 수 있다.
        for j in combinations(a, i):
            suma.append(sum(j))
    for i in range(len(b)+1):
        for j in combinations(b, i):
            sumb.append(sum(j))

    count = 0
    # suma 원소들 + sumb 원소들 <= c 인 가지 수 구하기
    sumb.sort() # 이진탐색을 위해 정렬하기
    for sa in suma:
        target = c-sa
        count += bisect_right(sumb, target)
    print(count)
solution()