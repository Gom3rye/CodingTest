import sys
input = sys.stdin.readline
def solution():
    n = int(input()) # 굴다리의 길이 <=100,000
    m = int(input()) # #가로등 <=100,000
    lights = list(map(int, input().split())) # 가로등의 위치
    answer, start, end = 0, 1, n
    while start <= end:
        mid = (start+end)//2 # 가로등의 최소 높이
        right = 0
        for x in lights:
            if right >= max(x-mid, 0):
                right = x+mid
            else:
                break
        if right >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
    print(answer)
solution()