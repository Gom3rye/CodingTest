import sys


n = int(sys.stdin.readline())
dp = [0, 1]

# 반복문을 통해 합이 n번째까지 제곱수들의 최소 개수를 구함.
for i in range(2, n + 1):
    target = 1e9

    # 반복문을 통해 최대 50000의 제곱을 확인
    for j in range(1, 50001):

        # 현재 수의 제곱이 i보다 크다면 멈춘다. i를 구하기 위함이므로
        if j ** 2 > i:
            break

        # n보다 작거나 같은 제곱수를 찾고 n-제곱수를 인덱스로 가진 값에 1을 더해주면 된다.
        target = min(target, dp[i - (j**2)])

    dp.append(target + 1)

print(dp[n])