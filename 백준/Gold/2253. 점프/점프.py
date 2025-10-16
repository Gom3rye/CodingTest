import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_list = []
for _ in range(m):
    a = int(input())
    n_list.append(a)

# n_list.sort()
# print(n_list)

max_speed = int((2 * n) ** 0.5) + 1

dp = [[float('inf')] * (max_speed+1) for _ in range(n+1)]
dp[1][0] = 0

def fun():

    for i in range(1, n+1):
        stone = i

        if stone in n_list:
            continue

        for j in range(1, max_speed):
            v = j
            dp[stone][v] = min(dp[stone - v][v-1], dp[stone - v][v], dp[stone - v][v+1]) + 1

    return dp

result = fun()
# print(result)
min_jumps = min(dp[n])
if min_jumps == float('inf'):
    print(-1)
else:
    print(min_jumps)