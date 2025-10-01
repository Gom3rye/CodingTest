import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [False]*n # dp[i]: i번 돌까지 도달할 수 있는지 여부
    dp[0] = True
    for i in range(n-1):
        if not dp[i]: # i번 돌에 도달할 수 있어야만 다음 점프 고려
            continue
        for j in range(i+1, n):
            power = (j-i)*(1+abs(arr[i]-arr[j]))
            if power <= k:
                dp[j] = True
    if dp[-1]:
        print("YES")
    else:
        print("NO")           
solution()