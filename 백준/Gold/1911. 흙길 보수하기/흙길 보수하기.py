import sys
import math
input = sys.stdin.readline
def solution():
    n, l = map(int, input().split()) # #물웅덩이 <=10,000, 길이 <=1,000,000
    puddles = [list(map(int, input().split())) for _ in range(n)]
    puddles.sort() # 시작 위치 기준으로 정렬, 제일 왼쪽을 기준으로 널빤지 놓기: 그리디
    # 시작 위치는 현재 널빤지의 오른쪽을 가리키는 포인터와 start의 max값!
    right = 0 # 널빤지 오른쪽
    answer = 0
    for start, end in puddles:
        left = max(right, start)
        if left < end:
            length = end-left # 길이는 항상 [start, end)
            cnt = math.ceil(length/l)
            answer += cnt
            right = left + cnt*l
    print(answer)
solution()