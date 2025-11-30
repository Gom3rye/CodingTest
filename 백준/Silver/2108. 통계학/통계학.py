import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    n = int(input())
    nums = sorted(int(input()) for _ in range(n))
    mean = round(sum(nums)/n) # round로 반올림 해주기
    print(mean)
    median = nums[n//2]
    print(median)
    counter = Counter(nums).most_common()
    mode_cnt = counter[0][1]
    # print(counter)
    mode = counter[1][0] if ((len(counter) > 1) and (counter[1][1] == mode_cnt)) else counter[0][0]
    print(mode)
    nums_range = nums[-1]-nums[0]
    print(nums_range)
solution()