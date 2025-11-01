import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solution():
    n = int(input()) # 원판의 개수
    def hanoi(cnt, start, dest, left):
        if cnt == 1:
            print(start, dest)
            return
        else:
            hanoi(cnt-1, start, left, dest)
            hanoi(1, start, dest, left)
            hanoi(cnt-1, left, dest, start)
    
    print(2**n-1)
    if n <= 20:
        hanoi(n, 1, 3, 2)
solution()