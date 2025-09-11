import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    n = int(input()) # 질문의 개수
    infos = [input().split() for _ in range(n)]
    def check(candidate, num): # 둘 다 문자열 오기
        check_strike, check_ball = 0, 0
        num_set = set(num)
        for i in range(3):
            if candidate[i] == num[i]:
                check_strike += 1
            elif candidate[i] in num_set:
                check_ball += 1
        return check_strike, check_ball

    # 가능한 순열 모두 만들어놓기
    candidates = []
    for i in permutations(range(1, 10), 3):
        candidates.append("".join(map(str, i)))

    result = set()
    for candidate in candidates:
        for num, strike, ball in infos:
            strike, ball = int(strike), int(ball)
            if strike == 3: # 지금 num 1개만 답이 될 수 있음
                print(1)
                return
            s, b = check(candidate, num)
            if strike != s or ball != b:
                break # 이 candidate는 정답이 될 수 없으므로
        else:
            result.add(candidate)
    print(len(result))
solution()