import sys

# 빠른 입력
input = sys.stdin.read
data = input().split()

# 데이터 파싱
n = int(data[0])
m = int(data[1])
numbers = list(map(int, data[2:n+2]))
queries = data[n+2:]

# 누적합 배열 생성
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + numbers[i]

# 결과 처리
output = []
for k in range(0, len(queries), 2):
    i = int(queries[k])
    j = int(queries[k+1])
    output.append(str(prefix_sum[j] - prefix_sum[i - 1]))

# 한 번에 출력
sys.stdout.write('\n'.join(output))
