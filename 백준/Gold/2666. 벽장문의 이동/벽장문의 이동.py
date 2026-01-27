n = int(input())
a, b = map(int, input().split())
m = int(input())
flow = []
dp = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    flow.append(int(input()))


def go(x, door1, door2):
    if x == m:
        return 0
    val = flow[x]
    dp[val][door1][door2] = min(
        abs(val - door1) + go(x+1, val, door2), abs(val - door2) + go(x+1, door1, val))
    return dp[val][door1][door2]

print(go(0, a, b))