def backtrack(start, seq):
    if len(seq) == m:
        print(*seq)
        return

    for i in range(start, n):
        backtrack(i, seq + [nums[i]])



n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

backtrack(0, [])