import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    grades = [list(map(int, input().split())) for _ in range(n)]
    # Step 1: 각 그레이드별로 책상에 존재하는지 표시
    has_grade = {g: [0]*n for g in range(1, 6)}

    for i in range(n):
        a, b = grades[i]
        has_grade[a][i] = 1
        has_grade[b][i] = 1

    max_len = 0
    min_grade = 6  # 그레이드 후보는 1~5

    # Step 2: 각 그레이드에 대해 최대 연속 구간 계산
    for g in range(1, 6):
        arr = has_grade[g]
        l = r = 0
        while r < n:
            # arr[i] == 1 이면 해당 책상에 그레이드 g가 있음
            if arr[r] == 1:
                r += 1
            else:
                l = r + 1
                r = l
            # 모든 책상에 그레이드 g가 있으면 학생 수는 r - l
            if r - l > max_len:
                max_len = r - l
                min_grade = g
            elif r - l == max_len:
                min_grade = min(min_grade, g)

    print(max_len, min_grade)
solution()