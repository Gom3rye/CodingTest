import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = arr[0]
    dp_removed = arr[0]
    result = arr[0]
    prev_dp = arr[0]  # ← 초기값 설정 필수

    for i in range(1, n):
        dp = max(arr[i], dp + arr[i])
        dp_removed = max(dp_removed + arr[i], prev_dp)
        prev_dp = dp  # ← 상태 저장은 마지막에 해야 함
        result = max(result, dp, dp_removed)

    print(result)

solution()
