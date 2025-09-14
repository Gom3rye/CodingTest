import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # 구간합 구하기
    cum = [0]*(n+1)
    for i in range(1, n+1):
        cum[i] = cum[i-1]+arr[i-1]
    for _ in range(m):
        i, j = map(int, input().split())
        print(cum[j]-cum[i-1])
solution()