def solution():
    N = int(input())
    L = list(map(int, input().split()))  # 체력 소모
    J = list(map(int, input().split()))  # 기쁨 얻기

    dp = [0] * 101  # dp[체력] = 최대 기쁨

    for i in range(N):
        for hp in range(100, L[i] - 1, -1):  # 뒤에서부터 갱신
            dp[hp] = max(dp[hp], dp[hp - L[i]] + J[i])

    print(max(dp[:100]))  # 체력이 1 이상인 경우만 고려 (0은 죽음)

solution()
