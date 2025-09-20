import sys
from itertools import product
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 가능한 모든 비밀번호의 개수를 구하는 것, 중복 순열
    cnt = 0
    for nums in product(range(10), repeat=n):
        for num in numbers:
            if num not in nums:
                break
        else:
            cnt += 1
    print(cnt)
solution()