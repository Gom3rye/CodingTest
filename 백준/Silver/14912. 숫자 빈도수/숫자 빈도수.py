import sys
input = sys.stdin.readline
def solution():
    n, d = map(int, input().split()) # 숫자, 숫자d의 빈도수
    cnt = 0
    for i in range(1, n+1):
        cnt += str(i).count(str(d))
    print(cnt)
solution()