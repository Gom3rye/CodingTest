import sys
from collections import defaultdict
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split()) #  같은 정수를 K개 이하로 포함한 최장 연속 부분 수열의 길이구하기
    a = list(map(int, input().split()))
    longest = 0
    start = 0
    count = defaultdict(int)
    for end in range(n):
        num = a[end]
        count[num] += 1 # 하나 선택
        while count[num] > k:
            count[a[start]] -= 1
            start += 1
 
        length = end - start + 1
        longest = max(longest, length)
    print(longest)
solution()