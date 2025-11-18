import sys
input = sys.stdin.readline
def solution():
    a, b, c = map(int, input().split())
    print(pow(a,b,c))
solution()