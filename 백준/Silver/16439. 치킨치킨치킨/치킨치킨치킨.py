import sys
from itertools import combinations
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 회원의 수, 치킨 종류의 수
    a = [list(map(int, input().split())) for _ in range(n)]
    max_preference = 0
    # 한 사람의 만족도는 "시킨 치킨 종류들 중에서 선호도가 가장 큰 값"으로 결정되니까 치킨의 3개의 종류를 먼저 고르고 확인해보기
    for chicken in combinations(range(m), 3):
        preference = 0
        for i in range(n):
            preference += max(a[i][c] for c in chicken)
        max_preference = max(max_preference, preference)
    print(max_preference)
solution()