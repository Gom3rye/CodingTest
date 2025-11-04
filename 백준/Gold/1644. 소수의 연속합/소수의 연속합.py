import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # <= 4,000,000
    cnt = 0
    def get_primes(n):
        sieve = [True]*(n+1)
        # 0,1 은 소수 아니니까 체에 False 기록
        sieve[0:2] = [False, False]
        limit = int(n**0.5)
        for i in range(2, limit+1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        return [i for i in range(2, n+1) if sieve[i]]
    # 연속합이 n인 경우의 수
    primes = get_primes(n)
    start = 0
    cnt = 0
    total = 0
    for end in range(len(primes)):
        total += primes[end]
        
        while total > n:
            total -= primes[start]
            start += 1
            
        if total == n:
            cnt += 1
    print(cnt)
solution()