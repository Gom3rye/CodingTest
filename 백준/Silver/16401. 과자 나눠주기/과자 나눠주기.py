import sys
input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())
    snacks = list(map(int, input().split()))

    left, right = 1, max(snacks)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        count = sum(s // mid for s in snacks)

        if count >= M:
            answer = mid  # 가능한 길이, 더 길게 해보자
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

solution()
