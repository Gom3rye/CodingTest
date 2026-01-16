import sys

def solution():
    input = sys.stdin.read().split()
    if not input: return
    n = int(input[0])
    nums = list(map(int, input[1:]))

    pos = []  # 1보다 큰 양수
    neg = []  # 0을 포함한 음수
    ones = 0  # 1의 개수 (1은 무조건 따로 더함)

    for num in nums:
        if num > 1:
            pos.append(num)
        elif num <= 0:
            neg.append(num)
        else:
            ones += 1

    # 양수는 큰 것끼리 곱해야 하므로 내림차순 정렬
    pos.sort(reverse=True)
    # 음수는 절대값이 큰 것(작은 수)끼리 곱해야 하므로 오름차순 정렬
    neg.sort()

    max_sum = 0

    # 1. 양수 처리
    for i in range(0, len(pos), 2):
        if i + 1 < len(pos):
            max_sum += (pos[i] * pos[i+1])
        else:
            max_sum += pos[i]

    # 2. 음수 처리 (0 포함)
    for i in range(0, len(neg), 2):
        if i + 1 < len(neg):
            max_sum += (neg[i] * neg[i+1])
        else:
            max_sum += neg[i]

    # 3. 1 처리
    max_sum += ones

    print(max_sum)

solution()