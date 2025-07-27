import bisect

def solution():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    children = [int(input()) for _ in range(N)]

    LIS = []

    for num in children:
        idx = bisect.bisect_left(LIS, num)
        if idx == len(LIS):
            LIS.append(num)
        else:
            LIS[idx] = num

    print(N - len(LIS))

solution()