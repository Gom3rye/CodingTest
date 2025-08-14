import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 추의 개수
    balance = list(map(int, input().split()))
    m = int(input()) # 구슬의 개수
    marbles = list(map(int, input().split()))
    dp = set([0])
    for chu in balance:
        temp = set()
        for i in dp:
            temp.add(i+chu)
            temp.add(abs(i-chu))
        dp |= temp # set union
    for marble in marbles:
        print('Y' if marble in dp else 'N', end=' ')
solution()