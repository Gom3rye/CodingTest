from collections import Counter
import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    # A의 모든 부분합 구하기
    sumA = []
    for i in range(n):
        temp = 0
        for j in range(i, n):
            temp += A[j]
            sumA.append(temp)

    # B의 모든 부분합 구하기
    sumB = []
    for i in range(m):
        temp = 0
        for j in range(i, m):
            temp += B[j]
            sumB.append(temp)

    # B 부분합을 Counter로 저장
    countB = Counter(sumB)

    # A 부분합마다 T - sumA 값을 B에서 찾기
    result = 0
    for a in sumA:
        result += countB[T - a]

    print(result)

solution()