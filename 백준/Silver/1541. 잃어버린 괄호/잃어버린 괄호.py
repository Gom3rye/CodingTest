import sys
input = sys.stdin.readline
def solution():
    expression = input().strip()
    # 최소를 만들려면 -를 기준으로 나눠서 빼주면 된다 -> 그리디
    nums = expression.split('-')
    answer = sum(map(int, nums[0].split('+')))
    for i in range(1, len(nums)):
        answer -= sum(map(int, nums[i].split('+')))
    print(answer)
solution()