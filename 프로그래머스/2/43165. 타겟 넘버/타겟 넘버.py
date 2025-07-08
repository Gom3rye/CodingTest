from itertools import product
def solution(numbers, target):
    n = len(numbers)
    count = 0
    for i in product(['+', '-'], repeat=n):
        result = 0 # 1 <= target 이니까
        for idx in range(n):
            if i[idx] == '+': # 첫 번째가 +라면 숫자만 고려
                result += numbers[idx]
            elif i[idx] == '-':
                result -= numbers[idx]
        if result == target:
            count += 1  
    return count