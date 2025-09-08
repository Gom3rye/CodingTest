import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    x = list(map(int, input().split()))
    start, end = 0, n-1
    max_score = 0
    while start < end:
        score = (end-start-1)*min(x[start], x[end])
        max_score = max(max_score, score)
        if x[start] < x[end]:
            start += 1
        else:
            end -= 1
    print(max_score)
solution()