import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #심사대 <=100,000, #사람 <=1,000,000,000
    took = [int(input()) for _ in range(n)]
    # 모두 검사받는 최솟값 구하기
    answer, start, end = float('inf'), 1, max(took)*m
    while start <= end:
        mid = (start+end)//2 # 심사를 마치는데 걸리는 최솟값
        cnt = 0
        for t in took:
            cnt += mid//t
            if cnt >= m:
                break

        if cnt >= m:
            answer = mid
            end = mid-1
        else:
            start = mid+1
    print(answer)
solution()