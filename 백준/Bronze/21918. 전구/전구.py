import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #전구, #명령 <=4000
    status = [-1]+list(map(int, input().split()))
    for _ in range(m):
        a, b, c = map(int, input().split())
        if a == 1:
            status[b] = c
        elif a == 2:
            status[b:c+1] = [i^1 for i in status[b:c+1]]
        elif a == 3:
            status[b:c+1] = [0]*(c-b+1)
        else:
            status[b:c+1] = [1]*(c-b+1)
    print(*status[1:])
solution()