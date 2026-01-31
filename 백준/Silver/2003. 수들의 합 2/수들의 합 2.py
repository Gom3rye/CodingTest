import sys
input = sys.stdin.readline
INF = float('inf')
def solution():
    n, m = map(int, input().split()) # #수 <=10000, 연속수열의 합(target) <=300,000,000
    arr = list(map(int, input().split()))
    cnt, now, start = 0, 0, 0
    for end in range(n):
        now += arr[end]
        while now > m:
            now -= arr[start]
            start += 1
        if now == m:
            cnt += 1
    print(cnt)
solution()