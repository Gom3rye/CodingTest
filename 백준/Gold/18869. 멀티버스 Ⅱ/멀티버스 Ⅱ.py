import sys
from collections import defaultdict
input = sys.stdin.readline
def solution():
    m, n = map(int, input().split()) # #우주 <=100, #행성 <=10000
    # 각 행성의 상대적인 크기만 필요한 거니까 크기로 랭킹을 매겨서 그 랭킹을 패턴의 키로 쓰고 해당 패턴을 가지고 있는 경우의 수가 총 몇개인지 파악!
    # 그 이후에 그 개수에서 조합 구하기
    pattern = defaultdict(int)
    for _ in range(m):
        universe = list(map(int, input().split()))
        # 크기로 랭킹을 매길 거니까 같은 숫자 없도록 set으로 받아주기
        sorted_universe = sorted(set(universe))
        # 이때 중요한 건(알고싶은 거) idx(순위)니까 rankings[size] = idx로 딕셔너리 초기화!
        rankings = {size: idx for idx, size in enumerate(sorted_universe)}
        pattern[tuple(rankings[size] for size in universe)] += 1
    
    cnt = 0
    for p in pattern.values():
        cnt += (p*(p-1)//2)
    print(cnt)
solution()