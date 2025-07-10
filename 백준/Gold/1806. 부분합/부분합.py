import sys
input = sys.stdin.readline
def solution():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    # 중요: 연속된 수들의 부분합
    min_len = int(1e9)
    start = 0
    # 최소 길이는 end-start+1 로 구하고 값은 result에 누적하면서 구하기
    result = 0
    for end in range(n):
        result += arr[end]
        # print(f"result: {result}, end: {end}")

        while result >= s:
            min_len = min(min_len, end-start+1)
            result -= arr[start]
            start += 1
            # print(f"start: {start}, end: {end}")
    print(min_len if min_len != int(1e9) else 0)
solution()