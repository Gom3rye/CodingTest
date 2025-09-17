def solution():
    N = int(input())
    result = []

    def dfs(num, last_digit):
        result.append(num)
        for next_digit in range(last_digit):
            dfs(num * 10 + next_digit, next_digit)

    for i in range(10):
        dfs(i, i)

    result.sort()
    
    if N > len(result):
        print(-1)
    else:
        print(result[N - 1])

solution()