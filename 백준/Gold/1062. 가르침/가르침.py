import sys
from itertools import combinations

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    
    if k < 5:
        print(0)
        return

    base = set(['a', 'n', 't', 'i', 'c'])
    word = [set(input().strip()[4:-4]) - base for _ in range(n)]
    
    w_set = set()
    for w in word:
        w_set |= w  # 배워야 할 모든 알파벳 모으기

    # 배워야 할 알파벳이 k-5개 이하이면, 전부 가르칠 수 있음
    if len(w_set) <= k - 5:
        print(n)
        return

    max_count = 0
    for comb in combinations(w_set, k - 5):
        teach = set(comb)
        count = 0
        for candidate in word:
            if candidate.issubset(teach):
                count += 1
        max_count = max(max_count, count)
    print(max_count)

solution()