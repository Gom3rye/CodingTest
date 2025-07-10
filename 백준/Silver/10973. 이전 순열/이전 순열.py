import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    num = list(map(int, input().split()))

    if prev_permutation(num):
        print(*num)
    else:
        print(-1)

def prev_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i-1] <= seq[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(seq) - 1
    while seq[j] >= seq[i-1]:
        j -= 1

    seq[i-1], seq[j] = seq[j], seq[i-1]
    seq[i:] = reversed(seq[i:])
    return True

solution()
