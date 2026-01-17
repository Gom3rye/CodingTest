import sys
input = sys.stdin.readline
def solution():
    # 수열을 적절히 묶어서 그 합이 최대가 되도록 하는 프로그램
    n = int(input()) # 수열의 크기 <=50
    arr = list(int(input()) for _ in range(n))
    # 1,음수(0),양수로 나누기
    ones = 0 # zeros는 왜 없어도 되냐면 0은 더해도 결과에 아무 영향을 주지 않기 때문
    positive, negative = [], []
    for num in arr:
        if num == 1: # 더하기가 무조건 낫다.
            ones += 1
        elif num <= 0:
            negative.append(num)
        else: # num > 0
            positive.append(num)
    positive.sort(reverse=True)
    negative.sort()
    max_result = 0
    pn = len(positive)
    for i in range(0, pn, 2): # 0~positive끝까지 2의 간격으로 탐색
        if i+1 < pn:
            max_result += positive[i]*positive[i+1]
        else: # 끝에 홀로 남은 마지막 원소
            max_result += positive[i]
    nn = len(negative)
    for i in range(0, nn, 2):
        if i+1 < nn:
            max_result += negative[i]*negative[i+1]
        else:
            max_result += negative[i]
    max_result += ones
    print(max_result)
solution()