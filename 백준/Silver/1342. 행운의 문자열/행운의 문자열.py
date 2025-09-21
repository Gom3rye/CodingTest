import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    s = input().strip()
    result = set()
    for string in permutations(s):
        for i in range(1, len(s)):
            if string[i] == string[i-1]:
                break
        else:
            result.add(''.join(string))
    print(len(result))
solution()