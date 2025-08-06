import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    nums = sorted(map(int, input().split()))
    good = 0
    for i in range(n):
        target = nums[i]
        left, right = 0, n-1
        while left < right:
            if left == i:
                left += 1
                continue
            if right == i:
                right -= 1
                continue
            current = nums[left]+nums[right]
            if current == target:
                good += 1
                break
            elif current < target:
                left += 1
            else:
                right -= 1
    print(good)
solution()