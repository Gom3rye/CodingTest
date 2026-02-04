import sys
from itertools import permutations
input = sys.stdin.readline
def solution(k, dungeons):
    # 최대 던전의 수가 8개이므로 완탐 가능! 8! = 40320
    n = len(dungeons)
    answer = -1
    for perm in permutations(range(n)):
        cnt = 0
        hp = k
        for p in perm:
            at_least, consumption = dungeons[p]
            if hp >= at_least:
                hp -= consumption
                cnt += 1
        answer = max(answer, cnt)
    return answer