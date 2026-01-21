import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    t = int(input()) # sum_target, [t] <=1,000,000,000
    na = int(input()) # <=1000
    a = list(map(int, input().split()))
    nb = int(input()) # <=1000
    b = list(map(int, input().split()))
    # 연속 배열쌍의 개수 구하기
    def prefix_sum(n, arr):
        sum_list = []
        for i in range(n):
            now = 0
            for j in range(i, n):
                now += arr[j]
                sum_list.append(now)
        return sum_list
    sum_a = prefix_sum(na, a)
    sum_b = prefix_sum(nb, b)
    sum_b_cnt = Counter(sum_b)
    answer = 0
    for sa in sum_a:
        answer += sum_b_cnt[t-sa]
    print(answer)
solution()