import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <=100,000
    sol = list(map(int, input().split())) # 오름차순으로 주어진다.
    # 가장 0에 가까운 용액 만들기
    start, end = 0, n-1
    answer = float('inf')
    abs_min = float('inf')
    while start < end:
        a, b = sol[start], sol[end]
        sum_sol = a+b
        if abs(sum_sol) < abs_min:
            abs_min = abs(sum_sol)
            answer = sum_sol
        if sum_sol < 0:
            start += 1
        elif sum_sol > 0:
            end -= 1
        elif sum_sol == 0:
            print(0)
            return
    print(answer)
solution()