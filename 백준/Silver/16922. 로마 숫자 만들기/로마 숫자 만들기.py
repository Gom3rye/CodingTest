import sys
input = sys.stdin.readline
n = int(input())
numbers = [1, 5, 10, 50]
result = set() # 만들 수 있는 수가 중복되면 안되니까.

# 중복 조합 backtracking으로 구현
def backtracking(s, depth, num):
    if depth == n:
        result.add(num)
        return
    for i in range(s, len(numbers)):
        num += numbers[i]
        backtracking(i, depth+1, num)
        num -= numbers[i]

backtracking(0,0,0) # start_idx, depth, total_num
print(len(result))