def solution(numbers, target):
    n = len(numbers)
    count = 0
    def backtracking(idx, result):
        nonlocal count
        if idx == n:
            if result == target:
                count += 1
            return
        
        backtracking(idx+1, result+numbers[idx])
        backtracking(idx+1, result-numbers[idx])
        
    backtracking(0, 0)
    return count