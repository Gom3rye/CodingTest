from itertools import combinations_with_replacement
from collections import Counter

def dist(a, b):
    return sum(x != y for x, y in zip(a, b))

def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        mbtis = input().split()

        # 비둘기집 원리: MBTI 16개, 각 유형 2명까지 → 32명까지 가능
        if n > 32:
            print(0)
            continue

        count = Counter(mbtis)
        if any(v >= 3 for v in count.values()):
            print(0)
            continue

        types = list(count.keys())
        min_dist = float('inf')

        for a, b, c in combinations_with_replacement(types, 3):
            needed = Counter([a, b, c])
            if all(count[t] >= needed[t] for t in needed):
                d = dist(a, b) + dist(b, c) + dist(a, c)
                min_dist = min(min_dist, d)

        print(min_dist)

solution()