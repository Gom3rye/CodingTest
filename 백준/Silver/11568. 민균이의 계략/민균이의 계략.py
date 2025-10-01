import sys
from bisect import bisect_left
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    # 순증가 최장 길이 구하기 (최장 증가 부분 수열 LIS)
    lis = [] # 현재까지 만들어진 LIS의 가장 작은 꼬리값들을 저장
    for num in arr:
        idx = bisect_left(lis, num)
        # print(idx)
        if idx == len(lis):
            lis.append(num)
            # print(lis)
        else:
            lis[idx] = num
    print(len(lis))
    # print(lis)
solution()