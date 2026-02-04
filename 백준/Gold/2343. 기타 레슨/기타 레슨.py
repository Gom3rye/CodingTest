import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split()) # #강의 <=100,000, #블루레이 <=n
    lectures = list(map(int, input().split()))
    max_l = max(lectures)
    # 가능한 블루레이크의 크기 중 최소 구하기
    answer, start, end = 0, max_l, max_l*n
    while start <= end:
        mid = (start+end)//2 # 블루레이크의 크기
        cnt, time = 1, 0
        for lecture in lectures:
            time += lecture
            if time > mid:
                cnt += 1
                time = lecture
        if cnt <= m:
            answer = mid
            end = mid-1
        else:
            start = mid+1

    print(answer)
solution()