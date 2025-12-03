import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        string = input().strip()
        if len(string) == 1:
            first = last = string[0]
        else:
            first, last = string[0], string[-1]
        print(first+last)
solution()