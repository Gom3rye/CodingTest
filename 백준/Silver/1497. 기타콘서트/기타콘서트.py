import sys
from itertools import combinations
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # 기타의 개수, 곡의 개수
    infos = [input().split() for _ in range(n)]
    max_play = 0
    guitar_cnt = 0 # 최소의 기타 개수(정답)
    for cnt in range(1, n+1):
        play = 0
        for chosen in combinations(range(n), cnt):
            songs = [False]*m
            for guitar in chosen:
                can_play = infos[guitar][1]
                for i in range(m):
                    if can_play[i] == 'Y' and not songs[i]:
                        songs[i] = True
            play = max(play, sum(songs))
        if play > max_play:
            max_play = play
            guitar_cnt = cnt

    print(guitar_cnt if guitar_cnt != 0 else -1)

solution()