import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    heights = []

    for _ in range(n):
        _, y = map(int, input().split())
        heights.append(y)

    stack = []
    count = 0

    for h in heights:
        while stack and stack[-1] > h:
            stack.pop()
            count += 1

        if stack and stack[-1] == h:
            continue

        if h > 0:
            stack.append(h)

    # 남아 있는 건물들 마무리
    count += len(stack)

    print(count)

solution()
