def find_sleep_spots():
    N = int(input())
    room = [input().strip() for _ in range(N)]

    horizontal = 0
    vertical = 0

    # 가로 탐색
    for i in range(N):
        count = 0
        for j in range(N):
            if room[i][j] == '.':
                count += 1
            else:
                if count >= 2:
                    horizontal += 1
                count = 0
        if count >= 2:
            horizontal += 1

    # 세로 탐색
    for j in range(N):
        count = 0
        for i in range(N):
            if room[i][j] == '.':
                count += 1
            else:
                if count >= 2:
                    vertical += 1
                count = 0
        if count >= 2:
            vertical += 1

    print(horizontal, vertical)

# 함수 호출 (제출 시 자동 호출됨)
find_sleep_spots()
