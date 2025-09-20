import sys
from itertools import permutations
input = sys.stdin.readline
def solution():
    s = input().strip()
    result = set()
    for string in permutations(s):
        for i in range(1, len(s)-1):
            if string[i] == string[i+1] or string[i] == string[i-1]:
                break
        else:
            lucky_string = ''.join(string)
            result.add(lucky_string)
    print(len(result))
solution()