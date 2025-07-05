import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))

def solution(arr, n):
    closest_sum = float('inf') # 무한대 설정
    result = []

    for i in range(n - 2):
        idx, start, end = i, i + 1, n - 1

        while start < end:
            total = arr[idx] + arr[start] + arr[end]

            if abs(total) < abs(closest_sum):
                closest_sum = total
                result = [arr[idx], arr[start], arr[end]]
            if total == 0:
                return sorted([arr[idx], arr[start], arr[end]])
            elif total < 0:
                start += 1
            else:
                end -= 1

    return sorted(result)

print(*solution(arr, n))