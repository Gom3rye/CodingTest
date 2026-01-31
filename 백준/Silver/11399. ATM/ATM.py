import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # #사람 <=1000
    times = sorted(map(int, input().split())) # 작은 시간부터 해야지 누적되는 결과값이 최소이다.
    # 누적합
    prefix_sum = [0]*(n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1]+times[i-1]
    print(sum(prefix_sum))
solution()