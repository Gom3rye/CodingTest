import sys

n, m, b = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
idx = 0
answer = sys.maxsize

for floor in range(257):
    max_block, min_block = 0, 0  # 초과분, 부족분

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= floor:  # 초과분 계산
                max_block += graph[i][j] - floor
            else:  # 부족분 계산
                min_block += floor - graph[i][j]

    if (max_block + b) >= min_block:  # floor층 개수로 평탄하게 할 수 있는지 체크(초과분 + 인벤토리의 블럭 수가 부족분보다 많으면 평탄하게 가능)
        if max_block * 2 + min_block <= answer:
            answer = max_block * 2 + min_block
            idx = floor  # 층수
print(answer, idx)