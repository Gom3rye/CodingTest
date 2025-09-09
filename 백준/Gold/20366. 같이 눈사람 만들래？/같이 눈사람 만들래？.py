import sys
from itertools import combinations
input = sys.stdin.readline
def solution():
    n = int(input())
    h = list(map(int, input().split()))
    min_diff = float('inf')
    # 눈사람 후보군 먼저 만들고
    possible_snowmen = []
    for i, j in combinations(range(n), 2):
        possible_snowmen.append((h[i]+h[j], i, j)) # (키, 인덱스i, 인덱스j)
    # 인접한 눈사람의 키가 비슷하도록 키 기준으로 정렬 -> (양옆만 확인해도 됨)
    possible_snowmen.sort()
    cnt = len(possible_snowmen) # 가능한 눈사람들의 개수
    for i in range(cnt-1):
        anna, ai, aj = possible_snowmen[i]
        elsa, ei, ej = possible_snowmen[i+1]
        # 서로의 인덱스가 곂치면 안된다.
        if len(set([ai, aj, ei, ej])) == 4:
            min_diff = min(min_diff, abs(anna-elsa))
            if min_diff == 0:
                break

    print(min_diff)
solution()