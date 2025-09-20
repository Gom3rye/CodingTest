import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())  # 기타 수, 곡 수
    infos = [input().split()[1] for _ in range(n)]  # Y/N 문자열만 추출

    max_play = 0
    min_guitar = float('inf')

    def dfs(idx, selected, songs):
        nonlocal max_play, min_guitar

        # 종료 조건: 모든 기타 확인했을 때
        if idx == n:
            play_cnt = songs.count(True)
            if play_cnt == 0:
                return
            if play_cnt > max_play:
                max_play = play_cnt
                min_guitar = selected
            elif play_cnt == max_play:
                min_guitar = min(min_guitar, selected)
            return

        # 선택하지 않는 경우
        dfs(idx + 1, selected, songs[:])

        # 선택하는 경우
        new_songs = songs[:]
        for i in range(m):
            if infos[idx][i] == 'Y':
                new_songs[i] = True
        dfs(idx + 1, selected + 1, new_songs)

    dfs(0, 0, [False] * m)

    print(min_guitar if max_play > 0 else -1)

solution()