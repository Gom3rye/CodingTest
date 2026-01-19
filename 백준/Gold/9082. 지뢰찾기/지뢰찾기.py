import sys
input = sys.stdin.readline
def solution():
    t = int(input()) # <=10
    for _ in range(t):
        n = int(input()) # <=100
        nums = list(map(int, input().strip()))
        _ = list(input().strip()) # 여기서는 중요x
        bombs = 0
        # bomb가 있는지 없는지는 nums[i-1],nums[i],nums[i+1]의 상태에 따라 달라진다.
        for i in range(n):
            if i == 0:
                if nums[i] != 0 and nums[i+1] != 0:
                    nums[i] -= 1
                    nums[i+1] -= 1
                    bombs += 1
            elif i == n-1:
                if nums[i-1] != 0 and nums[i] != 0:
                    nums[i-1] -= 1
                    nums[i] -= 1
                    bombs += 1
            else:
                if nums[i-1] != 0 and nums[i] != 0 and nums[i+1] != 0:
                    nums[i-1] -= 1
                    nums[i] -= 1
                    nums[i+1] -= 1
                    bombs += 1
        print(bombs)
solution()