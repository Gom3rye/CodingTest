import sys

# 입력
paper = [list(map(int, input().split())) for _ in range(10)]

# 색종이 사용 개수 (1~5 사이즈 색종이 각각 최대 5장)
papers = [0] * 6

# 덮어야 할 총 1의 개수
min_count = float('inf')

def can_attach(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != 1:
                return False
    return True

def attach(x, y, size, state):
    for i in range(x, x + size):
        for j in range(y, y + size):
            paper[i][j] = 0 if state else 1

def dfs(pos, count):
    global min_count

    # 가지치기: 이미 현재 경로가 더 많은 색종이를 썼다면 탐색 중지
    if count >= min_count:
        return

    # pos: 0~99까지의 좌표를 1차원 인덱스로 표현
    if pos == 100:
        min_count = count
        return

    x = pos // 10
    y = pos % 10

    if paper[x][y] == 1:
        for size in range(5, 0, -1):
            if papers[size] < 5 and can_attach(x, y, size):
                attach(x, y, size, True)
                papers[size] += 1
                dfs(pos + 1, count + 1)
                attach(x, y, size, False)
                papers[size] -= 1
    else:
        dfs(pos + 1, count)

# 실행
dfs(0, 0)

# 출력
print(min_count if min_count != float('inf') else -1)