import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dfs(number, depth):
    if depth == N:
        print(number)
        return
    for i in range(1, 10):
        next_number = number * 10 + i
        if is_prime(next_number):
            dfs(next_number, depth + 1)

N = int(input())
# 1자리 소수부터 시작
for prime in [2, 3, 5, 7]:
    dfs(prime, 1)
