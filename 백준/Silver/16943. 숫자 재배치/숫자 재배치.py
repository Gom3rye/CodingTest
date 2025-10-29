import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    a, b = input().split() # < 10^9 (9자리수까지 가능)
    answer = -1
    # b보다 작은 가장 큰 a의 순열 구하기
    if len(a) > len(b):
        print(answer)
        return
    # 9! = 약 36만 -> 완탐 가능
    for num in permutations(a):
        if num[0] == '0':
            continue
        result = ''.join(num)
        if int(result) < int(b):
            answer = max(answer, int(result))
    print(answer)
solution()
