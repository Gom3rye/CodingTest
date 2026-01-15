import sys
input = sys.stdin.readline
def solution():
    na, nb = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    result = sorted(a-b)
    print(len(result))
    print(*result)
solution()