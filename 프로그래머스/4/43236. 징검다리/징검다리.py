import sys
def solution(distance, rocks, n):
    # distance <=1,000,000,000
    rocks.sort() # 위치대로 배치, len(rocks) <=50000
    rocks.append(distance) # 출발점 추가
    # Parametric Search로 최대의 최솟값 구하기
    answer, start, end = 0, 1, 1000000000 
    while start <= end:
        mid = (start+end)//2 # ans 후보값
        now, removed = 0, 0 # 현재 바위, 지운 횟수
        for rock in rocks:
            if rock-now < mid:
                removed += 1
            else:
                now = rock # 그전이랑 이어가기
        
        if removed <= n: # n이하로 지우는 건 상관 없음(더 안 지울수록 최솟값이 작아지는 거니까)
            answer = mid
            start = mid+1
        else:
            end = mid-1
            
    return answer