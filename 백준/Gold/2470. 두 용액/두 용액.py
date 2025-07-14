import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = sorted(map(int, input().split()))
    result = float('inf')
    result_arr = []
    start, end = 0, n - 1

    while start < end:
        total = arr[start] + arr[end]
        if abs(total) < abs(result):
            result = total
            result_arr = [arr[start], arr[end]]
            if total == 0:  # 가장 좋은 케이스 조기 종료
                break
        if total < 0:
            start += 1
        else:
            end -= 1

    print(*result_arr)

solution()