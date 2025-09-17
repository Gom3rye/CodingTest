from collections import deque

def generate_decreasing_numbers():
    queue = deque()
    result = []

    for i in range(10):  # 한자리 줄어드는 수
        queue.append(i)

    while queue:
        num = queue.popleft()
        result.append(num)

        last_digit = num % 10
        for i in range(last_digit):
            next_num = num * 10 + i
            queue.append(next_num)

    return sorted(result)

def solution():
    N = int(input())
    dec_nums = generate_decreasing_numbers()
    if N > len(dec_nums):
        print(-1)
    else:
        print(dec_nums[N - 1])

solution()