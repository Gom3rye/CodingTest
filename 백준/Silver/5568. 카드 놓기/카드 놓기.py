import sys
from itertools import permutations

input = sys.stdin.readline

def solution():
    n = int(input())
    k = int(input())
    cards = [input().strip() for _ in range(n)]

    numbers = set()

    for perm in permutations(cards, k):
        num_str = ''.join(perm)
        numbers.add(num_str)

    print(len(numbers))

solution()
