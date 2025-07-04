from collections import Counter

def dist(a, b):
    return sum(x != y for x, y in zip(a, b))

def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        mbtis = input().split()
        count = Counter(mbtis)
        
        # 비둘기집 원리: MBTI 16개, 각 유형 2명까지 → 32명까지 가능
        if n > 32:
            print(0)
            continue
        # 같은 MBTI가 3명 이상이면 최소 거리 0
        if any(v >= 3 for v in count.values()):
            print(0)
            continue
        
        types = list(count.keys())
        min_dist = float('inf')
        
        # 중복 조합 (3개 선택) — combinations_with_replacement 대신, 직접 구현해도 됨
        for a in types:
            for b in types:
                for c in types:
                    if a <= b <= c:
                        # 각 MBTI 유형의 수가 충분한지 확인
                        needed = Counter([a, b, c])
                        if all(count[x] >= needed[x] for x in needed):
                            d = dist(a, b) + dist(b, c) + dist(a, c)
                            min_dist = min(min_dist, d)
        
        print(min_dist)
solution()