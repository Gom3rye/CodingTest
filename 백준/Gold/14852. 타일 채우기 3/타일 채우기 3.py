import sys

# 재귀 깊이 제한을 늘려줍니다.
sys.setrecursionlimit(10**6 + 10) 

N = int(sys.stdin.readline())
MOD = 1_000_000_007

# dp 테이블 초기화
# a[i]: 2xi 를 완전히 채우는 경우의 수
# b[i]: 2xi 에서 한 칸이 비는 경우의 수
a = [0] * (N + 1)
b = [0] * (N + 1)

# 초기값 설정
a[0] = 1
b[0] = 0

if N >= 1:
    a[1] = 2
    b[1] = 1

# 점화식을 이용해 DP 테이블 채우기
for i in range(2, N + 1):
    # b[i] = a[i-1] + b[i-1]
    b[i] = (a[i-1] + b[i-1]) % MOD
    
    # a[i] = 2*a[i-1] + a[i-2] + 2*b[i-1]
    term1 = (2 * a[i-1]) % MOD
    term2 = a[i-2]
    term3 = (2 * b[i-1]) % MOD
    
    a[i] = (term1 + term2 + term3) % MOD

# 최종 결과 출력
print(a[N])