import sys
input = sys.stdin.readline
def solution():
    n, h = map(int, input().split())
    crash = [0]*(h+2)
    for i in range(n):
        height = int(input())
        if i%2: # 홀수(위)
            crash[h-height+1] += 1
            crash[h+1] -= 1
        else: # 짝수(바닥)
            crash[1] += 1
            crash[height+1] -= 1
    # 누적합
    for i in range(1, h+1):
        crash[i] += crash[i-1]
    
    min_crash = min(crash[1:-1])
    print(min_crash, crash[1:-1].count(min_crash))
    
solution()