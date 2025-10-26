N, C, W = map(int, input().split())
lengths = [int(input()) for _ in range(N)]

max_len = max(lengths)
max_profit = 0

for L in range(1, max_len + 1):
    profit = 0
    for length in lengths:
        pieces = length // L
        if pieces == 0:
            continue
        cuts = pieces if length % L != 0 else pieces - 1
        money = pieces * L * W
        cost = cuts * C
        if money > cost:
            profit += (money - cost)
    max_profit = max(max_profit, profit)

print(max_profit)
