import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement
n = int(input())
numbers = [1, 5, 10, 50]
result = set() # 만들 수 있는 수가 중복되면 안되니까.

for num in combinations_with_replacement(numbers, n):
    total = sum(num)
    result.add(total)

print(len(result))