import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    start = 666
    th = 0
    while True:
        if '666' in str(start):
            th += 1
        if th == n:
            print(start)
            break
        start += 1
solution()