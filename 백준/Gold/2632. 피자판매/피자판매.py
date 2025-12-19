import sys
from collections import Counter
input = sys.stdin.readline
def solution():
    pizza_size = int(input()) # 피자크기 <=2,000,000
    m, n = map(int, input().split()) # a, b 피자조각 개수 <=1000
    a = list(int(input()) for _ in range(m))
    b = list(int(input()) for _ in range(n))
    # a의 누적합, b의 누적합 구하기
    def find_sum(arr):
        n = len(arr)
        arr2 = arr*2 # 원형에서 연속으로 이어진 구간의 합을 구해야 하니까
        prefix = [0]
        for x in arr2:
            prefix.append(prefix[-1] + x) # 누적합 갱신
        # 길이 1 ~ n-1
        sum_list = [0]
        for length in range(1, n):
            for start in range(n):
                sum_list.append(prefix[start+length] - prefix[start])
        # 총합도 꼭 잊지 말고 포함시켜주기!
        sum_list.append(sum(arr))
        return sum_list

    sum_a = find_sum(a)
    sum_b = find_sum(b)

    count_a = Counter(sum_a)
    count_b = Counter(sum_b)

    answer = 0 # 총 경우의 수
    for amount, cnt in count_a.items():
        left = pizza_size - amount
        answer += count_b[left]*cnt # cnt: count_a[amount]
    print(answer)

solution()