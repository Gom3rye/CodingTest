import sys
input = sys.stdin.readline
MOD = 1000000000
def solution():
    n = int(input()) # #힉셍 <=1,000,000
    # 완전순열 점화식: !n= (n−1)×(!(n−1)+!(n−2))
    # 초기값: !1 = 0, !2 = 1
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        d1 = 0 # !1
        d2 = 1 # !2
        for i in range(3, n+1):
            d = (i-1)*(d1+d2)%MOD
            d1, d2 = d2, d
        print(d)
solution()