import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

mistake = [0] * N
for i in range(N - 1):
    if A[i] > A[i + 1]:
        mistake[i + 1] = 1  # i와 i+1 사이에서 실수 발생

# 누적합 계산
prefix = [0] * (N)
for i in range(1, N):
    prefix[i] = prefix[i - 1] + mistake[i]

# 쿼리 처리
for _ in range(Q):
    x, y = map(int, input().split())
    print(prefix[y - 1] - prefix[x - 1])
