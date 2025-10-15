import sys
input = sys.stdin.readline

N = int(input().rstrip())
ground = [[0] * (N + 1)] +  [[0] + list(map(int, input().rstrip().split())) for _ in range(N)]
acc_sum = [[0] * (N + 1) for _ in range(N + 1)]

for row in range(1, N + 1):
    for col in range(1, N + 1):
        acc_sum[row][col] = ground[row][col] + acc_sum[row - 1][col] + acc_sum[row][col - 1] - acc_sum[row - 1][col - 1]

result = -sys.maxsize
for area in range(1, N + 1):
    for start_row in range(1, N - area + 2):
        for start_col in range(1, N - area + 2):
            end_row = start_row + area - 1
            end_col = start_col + area - 1

            area_sum = acc_sum[end_row][end_col] - acc_sum[start_row - 1][end_col] - acc_sum[end_row][start_col - 1] + acc_sum[start_row - 1][start_col - 1]
            result = max(result, area_sum)

print(result)