import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    n = int(input()) # #이닝 <=50 -> 충분히 작음, 브루트포스
    result = [list(map(int, input().split())) for _ in range(n)]
    # 1번 선수를 4번 타자로 하고 나머지 순열돌리기 # 0based index로 하면 0번 선수를 3번 타자로
    # 이닝은 3아웃이 되면 바뀌고 그 전까지는 계속 타순대로 순서 %9로 유지하며 시뮬
    def baseball(order):
        player_idx = 0
        score = 0
        for inning in range(n):
            out = 0
            base1 = base2 = base3 = 0 # 루에 있는 주자
            while out < 3:
                hit = result[inning][order[player_idx]]
                if hit == 0:
                    out += 1
                elif hit == 1:
                    score += base3
                    base3, base2, base1 = base2, base1, 1 # 주자가 들어왔을 때 1점이 올라가야 하니까 1로 표시
                elif hit == 2:
                    score += (base3+base2)
                    base3, base2, base1 = base1, 1, 0
                elif hit == 3:
                    score += (base3+base2+base1)
                    base3, base2, base1 = 1, 0, 0
                else: # hit == 4: 홈런
                    score += (base3+base2+base1+1)
                    base3 = base2 = base1 = 0

                player_idx = (player_idx+1)%9

        return score
    max_score = 0
    for perm in permutations(range(1, 9)): # 8!은 약 4만으로 완탐 가능
        order = perm[0:3]+(0,)+perm[3:] # 타순 결정
        score = baseball(order)
        max_score = max(max_score, score)
    print(max_score)
solution()