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
            for i in range(b, c+1):
                status[i]^=1 # toggle
        elif a == 3:
            for i in range(b, c+1):
                status[i] = 0
        else:
            for i in range(b, c+1):
                status[i] = 1
    print(*status[1:])
solution()