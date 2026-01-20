import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    # 수-등장횟수) 정렬 순: 등장횟수 오름차순, 수 오름차순
    r, c, k = map(int, input().split()) # <=100
    r, c = r-1, c-1 # 0based index
    # a[r][c]=k가 되기 위한 최소 시간 구하기, 100초가 지나도 안되면 -1출력
    a = [list(map(int, input().split())) for _ in range(3)]
    def matrix_sort(matrix):
        new_matrix = []
        max_len = 0
        for row in matrix:
            count = Counter(row) # 원소의 횟수 구하고
            sorted_count = sorted(count.items(), key=lambda x: (x[1], x[0])) # cnt, num 순으로 정렬
            new_row = [] # 한 줄로 이어 붙여야 하니까 append말고 extend로
            for num, cnt in sorted_count:
                if num == 0: # 0은 고려하지 않음
                    continue
                new_row.extend([num, cnt])
            new_row = new_row[:100] # 제한때문에 100개까지만
            max_len = max(max_len, len(new_row))
            new_matrix.append(new_row)
        # 남은 공간 0으로 채우기
        for row in new_matrix:
            row.extend([0]*(max_len-len(row)))
        return new_matrix

    time = 0
    while time <= 100:
        nr, nc = len(a), len(a[0])
        if r < nr and c < nc and a[r][c] == k: # IndexError 주의
            break
        if nr >= nc:
            a = matrix_sort(a) # a갱신 (new_matrix 만들어서 교체)
        else: # 열 연산 해야 함-> 전치 필요
            a = matrix_sort([list(row) for row in zip(*a)]) # 행<->열 바꿔서 계산 후
            a = [list(row) for row in zip(*a)] # 다시 행<->열 바꿔서 제출
        time += 1
    print(-1 if time>100 else time)
solution()