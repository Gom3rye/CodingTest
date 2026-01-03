import sys, heapq
from collections import Counter
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        n = int(input()) # #day <=1,000,000
        prices = list(map(int, input().split()))
        # 언제가 최대값일지 모름(미래의 일이라서) => 뒤에서부터 생각하자.
        # 관점: "이때 팔려면 이전에 얼마였어야 할까?" -> 이미 지나온 길이 미래이므로 현재까지의 최댓값이 곧 미래의 최고가임.
        max_price = -1
        max_profit = 0
        for i in range(n-1, -1, -1):
            if max_price < prices[i]:
                max_price = prices[i]
            else:
                max_profit += max_price-prices[i]
        print(max_profit)
solution()