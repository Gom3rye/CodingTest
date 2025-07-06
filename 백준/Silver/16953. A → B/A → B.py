import sys
input = sys.stdin.readline
def solution():
    a, b = map(int, input().split()) # a를 b로 바꾸기
    count = 1
    while b != a:
        if b%10 == 1:
            b = b//10
            count += 1
        elif b%2 == 0 and b != 0:
            b = b//2
            count += 1
        else:
            count = -1
            break
    print(count)
solution()