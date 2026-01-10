import sys
input = sys.stdin.readline
def solution():
    s = input().strip() # <= 1,000,000
    explode = list(input().strip()) # <= 36
    stack = []
    n, last = len(explode), explode[-1]
    for char in s:
        stack.append(char)
        while char == last and stack[-n:] == explode:
            del stack[-n:]
    if stack:
        print("".join(stack))
    else:
        print("FRULA")
solution()