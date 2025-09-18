def solution():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    dp = [0] * N
    for i in range(N):
        dp[i] = A[i]  # 초기값: 자기 자신
        for j in range(i):
            if A[j] > A[i]:
                dp[i] = max(dp[i], dp[j] + A[i])

    print(max(dp))

solution()
