import sys
from collections import defaultdict
input = sys.stdin.readline
INF = float('inf')
def solution():
    s = input().strip()
    n = len(s) # <=50
    # s에 있는 문자를 알파벳 순으로 입력하는 최소 누름 횟수
    # 우선 s를 이루는 알파벳들의 각각의 위치 저장해놓기
    char_pos = defaultdict(list)
    for i, char in enumerate(s):
        char_pos[char].append(i)
    # s를 이루는 알파벳들만 순서대로 정렬
    sorted_char = sorted(char_pos.keys())
    # dp[i][pos]: i번째 단어를 모두 처리하고 pos위치에서 끝낸 최소 횟수
    dp = [] # sort했기 때문에 a부터 0번째, b=1, c=2 이렇게 인덱스로 접근할 수 있다.
    for char in sorted_char:
        dp.append([INF]*len(char_pos[char]))
    # 0에서 출발해서 첫번째 단어만 처리한 로직 minx->maxx 거나 maxx->minx로 단방향으로 가는게 가장 최소의 비용이다. (왼쪽갔다 오른쪽갔다 왼쪽갔다 이렇게 와리가리 x)
    first_char = sorted_char[0]
    first_pos = char_pos[first_char]
    min_x, max_x = min(first_pos), max(first_pos)
    for i, p in enumerate(first_pos):
        # 0 -> min -> max -> p로 가는 경우
        dist1 = min_x + max_x-min_x +abs(p-max_x)
        # 0 -> max -> min -> p로 가는 경우
        dist2 = max_x + max_x-min_x+ abs(p-min_x)
        dp[0][i] = min(dist1, dist2)
    # 이제 각자 cur_x, prev_x 에 의한 모든 조합을 고려하며 최소값 탐색
    for char_i in range(1, len(sorted_char)):
        prev_char, cur_char = sorted_char[char_i-1], sorted_char[char_i]
        prev_pos, cur_pos = char_pos[prev_char], char_pos[cur_char]
        min_x, max_x = min(cur_pos), max(cur_pos)
        for cur_i, cur_p in enumerate(cur_pos):
            for prev_i, prev_p in enumerate(prev_pos):
                # prev_p -> min_x -> max_x -> cur_p로 가는 경우
                dist1 = abs(min_x-prev_p) + max_x-min_x + abs(max_x-cur_p)
                # prev_p -> max_x -> min_x -> cur_p로 가는 경우
                dist2 = abs(max_x-prev_p) + max_x-min_x + abs(min_x-cur_p)
                dp[char_i][cur_i] = min(dp[char_i][cur_i], dp[char_i-1][prev_i]+min(dist1, dist2))
    print(min(dp[-1])+n)
solution()