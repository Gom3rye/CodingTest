import sys
input = sys.stdin.readline
def solution():
    n, c, w = map(int, input().split()) # 나무의 개수, 자르는 비용, 한 단위의 가격
    # 버는 돈: k(개)*l(길이)*w(한 단위 가격) - c*m(자르는 횟수) -> 이를 위해 알아야 하는 것: 나무의 길이(길이가 정해지면 개수와 자르는 횟수도 정해진다.)
    trees = [int(input()) for _ in range(n)]
    max_len = max(trees)
    answer = 0
    # 길이만 정하면 되니까 완탐으로 구하기
    for l in range(1, max_len+1): # <= 10000
        total_profit = 0
        for tree in trees: # <= 50 따라서 완탐 가능
            k = tree//l # 개수
            if k == 0: # 1조각도 안 나오면 스킵
                continue
            if tree%l == 0: # 딱 길이로 나눠떨어지면
                m = k-1 # 자르는 횟수
            else:
                m = k
            profit = k*l*w - c*m
            if profit > 0:
                total_profit += profit
        answer = max(answer, total_profit)
    print(answer)
solution()